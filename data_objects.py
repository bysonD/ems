from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, name:str):
        self.id = ""
        self.name = name
        from repository import Repository
        Repository.add(self)

    def get_dict(self):
        result = dict()
        for key, value in self.__dict__.items():
            if isinstance(value, list):
                result[key] = [member.get_id() for member in value]
            elif hasattr(value, "id"):
                result[key] = value.get_id()
            else:
                result[key] = value

        return result

        
    
    @abstractmethod
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    @abstractmethod
    def __str__(self):
        return f"Name: {self.name}"
    
    @staticmethod
    def get_list_members(proper_list:list):
        if proper_list:
            temp_str = ", ".join(member.get_name() for member in proper_list) or "No data."
            return temp_str
        
    
class Department(BaseModel):
    def __init__(self, name):
        super().__init__(name)
        self.manager = None
        self.teams = []
        self.members = []
        self.jobs = []

    def add_to_list(self, obj):
        if isinstance(obj, Team):
            self.teams.append(obj)
        elif isinstance(obj, JobPosition):
            self.jobs.append(obj)
        elif isinstance(obj, Employee):
            self.members.append(obj)

    def add_manager(self, manager):
        self.manager = manager

    def create_team(self, name:str, members:list=None):
        temp_team = Team(name, self)
        if members:
            for member in members:
                temp_team.add_to_team(member)
        return f"New team {temp_team.get_name()} has been succesfully created at department {self.get_name()}."

    def get_name(self):
        return super().get_name()
    
    def __str__(self):
        if self.manager:
            temp_man = self.manager.get_name()
        else:
            temp_man = "No manager"
        return f"""DEPARTMENT
{super().__str__()}
Manager: {temp_man}
    Members: {self.get_list_members(self.members)}
    Teams: {self.get_list_members(self.teams)}
    Jobs: {self.get_list_members(self.jobs)}"""

class Team(BaseModel):
    def __init__(self, name, department:Department = None):
        super().__init__(name)
        self.members = []
        self.department = department
        department.add_to_list(self)

    def add_to_team(self, member):
        self.members.append(member)

    def get_name(self):
        return super().get_name()
    
    def __str__(self):
        return f"""{super().__str__()}
Members: {self.get_list_members(self.members)}
Department: {self.department.get_name()}"""
    
class JobPosition(BaseModel):
    levels = ["Junior", "Medior", "Senior"]
    def __init__(self, name, level:str, department:Department = None):
        super().__init__(name)
        self.level = level
        self.department = department
        department.add_to_list(self)

    def get_name(self):
        return f"{self.level} {self.name}"
    
    def __str__(self):
        return f"""Position: {self.get_name()}
Department: {self.department.get_name()}"""
    
class Employee(BaseModel):
    def __init__(self, name, surname:str, salary:int):
        super().__init__(name)
        self.surname = surname
        self.set_salary(salary)
    
    def set_salary(self, amount):
        if amount > 0:
            self.salary = amount
        else:
            raise ValueError(f"Salary cannot be a negative number!")
        
    def get_salary(self):
        return self.salary
        
    def get_name(self):
        return f"{self.name} {self.surname}"
    
    def __str__(self):
        return f"""{super().__str__()}
Surname: {self.surname}
Salary: {self.salary} €/month""" 
    
class Worker(Employee):
    def __init__(self, name, surname, salary, job:JobPosition = None):
        self.role = "Worker"
        super().__init__(name, surname, salary)
        self.job = job
        job.department.add_to_list(self)

    def get_name(self):
        return super().get_name()
    
    def __str__(self):
        return f"""{super().__str__()}
Department: {self.job.department.get_name()}
Position: {self.job.get_name()}"""   

class Manager(Employee):
    def __init__(self, name, surname, salary, dep:Department = None):
        self.role = "Manager"
        super().__init__(name, surname, salary)
        self.department = dep
        self.department.add_manager(self)

    def get_name(self):
        return super().get_name()
    
    def hire_new_worker(self, name:str, surname:str, salary:int, job:JobPosition):
        temp_worker = Worker(name, surname, salary, job)
        return f"New worker {temp_worker.get_name()} has been succesfully hired at {temp_worker.job.department.get_name()} department.\n"
    
    def change_workers_salary(self, worker:Worker, amount:int):
        temp_sal = worker.get_salary()
        worker.set_salary(amount)
        return f"Salary of worker {worker.get_name()} has been changed from {temp_sal} to {worker.get_salary()}.\n"
    
class Leader(Employee):
    def __init__(self, name, surname, salary):
        self.role = "Leader"
        super().__init__(name, surname, salary)
        self.departments: list[Department] = []

    def add_department(self, department:Department):
        self.departments.append(department)

    def create_new_department(self, name:str):
        temp_dep = Department(name)
        return f"Department {temp_dep.get_name()} has been succesfully created.\n"

    @staticmethod
    def get_manager(dep:Department):
        if dep.manager:
            return f"Current manager of department {dep.get_name()} is {dep.manager.get_name()}.\n"
        else:
            return f"Department {dep.get_name()} has no manager.\n"

    def set_manager(self,dep:Department, new_manager:Manager):
        self.get_manager(dep)
        dep.add_manager(new_manager)
        return f"New manager of department {dep.get_name()} is {new_manager.get_name()}.\n"
    
    def get_managers(self):
        list_of_mans = []
        if self.departments:
            for record in self.departments:
                list_of_mans.append(record.manager)
            return list_of_mans
        else:
            raise IndexError("No departments found!\n")
        
    @staticmethod
    def change_managers_salary(manager:Manager, amount:int):
        temp_sal = manager.get_salary()
        manager.set_salary(amount)
        return f"Salary of manager {manager.get_name()} has been changed from {temp_sal} to {manager.get_salary()}.\n"
    
    
    def get_name(self):
        return super().get_name()

if __name__ == "__main__":
    dep2 = Department("IT")
    result_dict = dep2.get_dict()

    print(f"""__dict__
{dep2.__dict__}\n""")
    print(f"""get_dict()
{result_dict}""")

"""
dep2 = Department("IT")
dep = Department("Marketing")

jp = JobPosition("Programator", JobPosition.levels[3], dep2)
jp2 = JobPosition("Strihac", JobPosition.levels[3], dep)

man = Manager("Miro","Pele", 2500, jp)
man2 = Manager("Juro", "Jantar", 2200, jp2)

lidr = Leader("Palo", "Scerba", 3600)
lidr.add_department(dep)
lidr.add_department(dep2)
"""
