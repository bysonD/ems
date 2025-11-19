from repository import Repository
from data_objects import Department, Team, JobPosition, Leader, Manager, Worker
from global_utils import default_warning, list_hint, id_input_message, SEPARATOR_MULTIPLIER, not_in_list_warning
from logger import DEF_LOGGER

# help methods
def dict_lookup(repo_list:list):
    return {res.get_id(): res for res in repo_list}

def get_list_ids(repo_list:list):
    result = []
    for record in repo_list:
        result.append(record.get_id())
    return result

# methode for work with individual instances
def get_instance_by_id(input_id:str, instance_list:list):
    ids_list = get_list_ids(instance_list)
    instance_lookup = dict_lookup(instance_list)
    if input_id in instance_lookup:
        instance = instance_lookup.get(input_id)
        return instance
    else:
        print(not_in_list_warning(ids_list))
        return None

# listing method
def list_instances(selected_list:list):
    if selected_list:
        for record in selected_list:
            print(record)
            print("-"*SEPARATOR_MULTIPLIER)
    else:
        print("No records to view in list.")

# creation methods
def create_department():
    name = input("Name of Department: ")
    temp_dep = Department(name)
    print(f"New Department [{temp_dep.introduce()}] has been succesfully created.")

def create_team():
    name = input("Name: ")
    dep_id = input(f"{list_hint(Repository.departments)}\nDepartment ID: ")
    deps = dict_lookup(Repository.departments)
    deps_ids = get_list_ids(Repository.departments)
    if dep_id in deps_ids:
        dep = deps.get(dep_id)
        temp_team = Team(name, dep)
        DEF_LOGGER.log(f"New Team [{temp_team.introduce()}] has been succesfully created at department: {temp_team.department}.")
    else:
        default_warning()
    
def create_worker(name:str, surname:str, salary:int, job:JobPosition):
    temp_worker = Worker(name, surname, salary, job)
    print(f"New Worker [{temp_worker.introduce()}] has been succesfully hired at job position: {temp_worker.job}.")

def create_job(name:str, level:str, dep:Department):
    temp_job = JobPosition(name, level, dep)
    print(f"New Job Position [{temp_job.introduce()}] has been succesfully created at department: {temp_job.department}.")

def create_manager(name:str, surname:str, salary:int):
    temp_man = Manager(name, surname, salary)
    print(f"New Manager [{temp_man.introduce()}] has been succesfully hired.")

def create_leader():
    name = input("Name: ")
    surname = input("Surname: ")
    salary = input("Salary: ")
    try:
        salary = int(salary)
    except ValueError:
        default_warning()
    temp_leader = Leader(name, surname, salary)
    print(f"New Leader [{temp_leader.introduce()}] has been succesfully hired.")

# custom methods
def add_member_to_team(team):
    pass

def change_salary_of_worker(manager, worker):
    pass

def set_new_manager(manager, department):
    pass

def change_salary_of_manager(leader, manager):
    pass