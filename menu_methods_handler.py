from repository import Repository
from data_objects import Department, Team, JobPosition, Leader, Manager, Worker
from global_utils import default_warning, SEPARATOR_MULTIPLIER, not_in_list_warning, base_list_hint, warning_out_of_range, clear_terminal, list_hint
from logger import DEF_LOGGER

# help methods
def dict_lookup(repo_list:list):
    return {res.get_id(): res for res in repo_list}

def get_list_ids(repo_list:list):
    result = []
    for record in repo_list:
        result.append(record.get_id())
    return result

def check_index(index_to_check, list_to_check:list):
    try:
        index_to_check = int(index_to_check)-1
    except ValueError:
        print(default_warning())
        return

    if not (0 <= index_to_check < len(list_to_check)):
        print(warning_out_of_range(1, len(list_to_check)))
        return
    
    return index_to_check

def import_starter_method():
    from starter import starter
    starter()
    print("\nStarting data were succesfully imported.\n")

    confirmation()

def save_and_exit():
    from file_handler import save_repository_to_files
    save_repository_to_files()
    print("All data saved to files exiting...")
    exit()

def confirmation():
    input("Press [ENTER] to continue...")
    clear_terminal()

# methode for work with individual instances
def get_instance_by_id(input_id:str, instance_list:list):
    ids_list = get_list_ids(instance_list)
    instance_lookup = dict_lookup(instance_list)
    if input_id in instance_lookup:
        instance = instance_lookup.get(input_id)
        return instance
    else:
        print(not_in_list_warning(ids_list))

# listing method
def list_instances(selected_list:list):
    if selected_list:
        for record in selected_list:
            print(record)
            print("-"*SEPARATOR_MULTIPLIER)
    else:
        print("No records to view in list.")

# creation methods
def create_instance_base():
    print("-"*SEPARATOR_MULTIPLIER)
    return input("Name: ")

def create_department(leader: Leader):
    name = create_instance_base()
    DEF_LOGGER.log(leader.create_new_department(name))
    confirmation()

def create_team(dep: Department):
    name = create_instance_base()
    DEF_LOGGER.log(dep.create_team(name))
    confirmation()
    
def create_worker(man: Manager):
    name = create_instance_base()
    surname = input("Surname: ")

    dep = man.department
    print(list_hint(dep.jobs))
    u_input = input("Job: ")
    u_input = check_index(u_input, dep.jobs)
    
    try:
        salary = int(input("Salary: "))
        DEF_LOGGER.log(man.hire_new_worker(name, surname, salary, dep.jobs[u_input]))
    except ValueError:
        print(default_warning())
    
    confirmation()

def create_job(dep: Department):
    name = create_instance_base()
    levels = JobPosition.levels

    print(base_list_hint(levels))

    u_input = input("Level: ")
    u_input = check_index(u_input, levels)

    DEF_LOGGER.log(dep.create_job(name, levels[u_input]))
    confirmation()


def create_manager(leader: Leader):
    name = create_instance_base()
    surname = input("Surname: ")
    try:
        salary = int(input("Salary: "))
        DEF_LOGGER.log(leader.hire_new_manager(name, surname, salary))
    except ValueError:
        print(default_warning())

    confirmation()

def create_leader():
    name = create_instance_base()
    surname = input("Surname: ")
    try:
        salary = int(input("Salary: "))
        leader = Leader(name, surname, salary)
        DEF_LOGGER.log(f"New Leader [{leader.introduce()}] has been succesfully hired.")
    except ValueError:
        print(default_warning())

    confirmation()

# custom methods
def add_member_to_team(team:Team):
    av_members = team.department.members
    print(list_hint(av_members))

    u_input = input("Member: ")
    u_input = check_index(u_input, av_members)
    selected_member = av_members[u_input]

    if not selected_member in team.members:
        team.add_to_team(selected_member)
        DEF_LOGGER.log(f"[{selected_member.introduce()}] has been succesfully addded to the [{team.introduce()}] team.")
    else:
        print(f"Member [{selected_member.introduce()}] already has a team assigned!")
    
    confirmation()

def set_new_manager(leader: Leader):
    deps = leader.departments
    if deps:
        managers = Repository.managers
        print(list_hint(deps))

        dep_input = input("Department: ")
        dep_input = check_index(dep_input, deps)
        selected_dep = deps[dep_input]
        print(selected_dep.introduce())

        print(list_hint(managers))
        man_input = input("Manager: ")
        man_input = check_index(man_input, managers)
        selected_man = managers[man_input]
        print(selected_man.introduce())

        DEF_LOGGER.log(leader.set_manager(selected_dep, selected_man))
    else:
        print("No departments available.\n")

    confirmation()

def change_salary_of_worker(manager:Manager):
    workers = manager.department.members
    if workers:
        print(list_hint(workers))

        u_input = input("Worker: ")
        u_input = check_index(u_input, workers)
        selected_worker = workers[u_input]
        print(f"Worker [{selected_worker.introduce()}] has current salary of: {selected_worker.get_salary()} €")

        try:
            salary_input = int(input("New salary: "))
            DEF_LOGGER.log(manager.change_workers_salary(selected_worker, salary_input))
        except ValueError:
            print(default_warning())
    else:
        print("\nNo workers available.\n")

    confirmation()

def change_salary_of_manager(leader: Leader):
    managers = leader.get_managers()
    if managers:
        print(list_hint(managers))

        u_input = input("Manager: ")
        u_input = check_index(u_input, managers)
        selected_manager = managers[u_input]
        print(f"Manager [{selected_manager.introduce()}] has current salary of: {selected_manager.get_salary()} €")

        try:
            salary_input = int(input("New salary: "))
            DEF_LOGGER.log(leader.change_managers_salary(selected_manager, salary_input))
        except ValueError:
            print(default_warning())
    else:
        print("\nNo managers available.\n")

    confirmation()

# log methods
def load_log(file):
    with file.open("r", encoding="utf-8") as f:
        print(f"\n{f.read()}")

    confirmation()
