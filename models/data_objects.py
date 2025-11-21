from abc import ABC, abstractmethod

class BaseModel(ABC):
    counter = 1
    def __init__(self, name:str):
        self.id = ""
        self.name = name
        from models.repository import Repository
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
    
    @classmethod
    def get_counter(cls):
        return cls.counter
    
    @classmethod
    def set_counter(cls, value:int = None):
        if value:
            cls.counter = value
        else:
            cls.counter = 1

    @classmethod
    def generate_id(cls, prefix:str):
        return prefix + str(cls.counter)
       
    @abstractmethod
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def introduce(self):
        return f"{self.get_id()} | {self.get_name()}"
    
    @abstractmethod
    def __repr__(self):
        return f"""ID: {self.id}
Name: {self.name}"""
    
    @staticmethod
    def get_list_members(proper_list:list):
        if proper_list:
            temp_str = ", ".join(member.get_name() for member in proper_list) or "No data."
            return temp_str
        
    
class Department(BaseModel):
    def __init__(self, name):
        super().__init__(name)
        self.id = self.generate_id("D")
        self.manager = None
        self.teams = []
        self.members = []
        self.jobs = []
        Department.counter += 1

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
        return f"New team [{temp_team.introduce()}] has been succesfully created at department [{self.introduce()}]."
    
    def create_job(self, name:str, level:str):
        temp_job = JobPosition(name, level, self)
        return f"New job [{temp_job.introduce()}] has been succesfully created at department [{self.introduce()}]."

    def get_name(self):
        return super().get_name()
    
    def __repr__(self):
        if self.manager:
            temp_man = self.manager.get_name()
        else:
            temp_man = "No manager"
        return f"""DEPARTMENT
{super().__repr__()}
Manager: {temp_man}
    Members: {self.get_list_members(self.members)}
    Teams: {self.get_list_members(self.teams)}
    Jobs: {self.get_list_members(self.jobs)}"""

class Team(BaseModel):
    def __init__(self, name, department:Department = None):
        super().__init__(name)
        self.id = self.generate_id("T")
        self.members = []
        self.department = department
        if department:
            department.add_to_list(self)
        Team.counter += 1

    def add_to_team(self, member):
        self.members.append(member)

    def get_name(self):
        return super().get_name()
    
    def __repr__(self):
        return f"""{super().__repr__()}
Members: {self.get_list_members(self.members)}
Department: {self.department.get_name()}"""
    
class JobPosition(BaseModel):
    levels = ["Junior", "Medior", "Senior"]
    def __init__(self, name, level:str, department:Department = None):
        super().__init__(name)
        self.id = self.generate_id("J")
        self.level = level
        self.department = department
        if department:
            department.add_to_list(self)
        JobPosition.counter += 1

    def get_name(self):
        return f"{self.level} {self.name}"
    
    def __repr__(self):
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
    
    def __repr__(self):
        return f"""{super().__repr__()}
Surname: {self.surname}
Salary: {self.salary} €/month""" 
    
class Worker(Employee):
    def __init__(self, name, surname, salary, job:JobPosition = None):
        self.role = "Worker"
        super().__init__(name, surname, salary)
        self.id = self.generate_id("W")
        self.job = job
        if job:
            job.department.add_to_list(self)
        Worker.counter += 1

    def get_name(self):
        return super().get_name()
    
    def __repr__(self):
        return f"""{super().__repr__()}
Department: {self.job.department.get_name()}
Position: {self.job.get_name()}"""   

class Manager(Employee):
    def __init__(self, name, surname, salary, dep:Department = None):
        self.role = "Manager"
        super().__init__(name, surname, salary)
        self.id = self.generate_id("M")
        self.department = dep
        if dep:
            self.department.add_manager(self)
        Manager.counter += 1

    def get_name(self):
        return super().get_name()
    
    def set_department(self, dep:Department):
        self.department = dep
    
    def hire_new_worker(self, name:str, surname:str, salary:int, job:JobPosition):
        temp_worker = Worker(name, surname, salary, job)
        return f"New worker [{temp_worker.introduce()}] has been succesfully hired at {temp_worker.job.department.get_name()} department.\n"
    
    def change_workers_salary(self, worker:Worker, amount:int):
        temp_sal = worker.get_salary()
        worker.set_salary(amount)
        return f"Salary of worker [{worker.introduce()}] has been changed from {temp_sal} to {worker.get_salary()}.\n"
    
class Leader(Employee):
    def __init__(self, name, surname, salary):
        self.role = "Leader"
        super().__init__(name, surname, salary)
        self.id = self.generate_id("L")
        self.departments: list[Department] = []
        Leader.counter += 1

    def add_departments(self, *args:Department):
        for department in args:
            self.departments.append(department)

    def create_new_department(self, name:str):
        temp_dep = Department(name)
        return f"Department [{temp_dep.introduce()}] has been succesfully created by leader [{self.introduce()}]."
    
    def hire_new_manager(self, name:str, surname:str, salary:int):
        temp_man = Manager(name, surname, salary)
        return f"New manager [{temp_man.introduce()}] has been succesfully hired by leader [{self.introduce()}]."

    def set_manager(self, dep:Department, new_manager:Manager):
        dep.add_manager(new_manager)
        new_manager.set_department(dep)
        return f"New manager of department [{dep.introduce()}] is [{new_manager.introduce()}]."
    
    def get_managers(self):
        if not self.departments:
            print("No departments found, cannot proceed this action.")
            return []
        
        list_of_mans = []
        for record in self.departments:
            list_of_mans.append(record.manager)

        return list_of_mans
        
    @staticmethod
    def change_managers_salary(manager:Manager, amount:int):
        temp_sal = manager.get_salary()
        manager.set_salary(amount)
        return f"Salary of manager [{manager.introduce()}] has been changed from {temp_sal} to {manager.get_salary()}.\n"
    
    
    def get_name(self):
        return super().get_name()

if __name__ == "__main__":
    dep2 = Department("IT")
    result_dict = dep2.get_dict()

    print(f"""__dict__
{dep2.__dict__}\n""")
    print(f"""get_dict()
{result_dict}""")
