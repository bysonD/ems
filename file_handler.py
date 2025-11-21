import json
from models.repository import Repository
from models.data_objects import (
    Department, 
    Team, 
    JobPosition, 
    Worker, 
    Manager, 
    Leader
)

SAVE_FOLDER = "data_files/"

ID_COUNTER_FILE = f"{SAVE_FOLDER}id_counter.json"

FILES = {
"departments": f"{SAVE_FOLDER}departments.json",
"teams": f"{SAVE_FOLDER}teams.json",
"jobs": f"{SAVE_FOLDER}jobs.json",
"workers": f"{SAVE_FOLDER}workers.json",
"managers": f"{SAVE_FOLDER}managers.json",
"leaders": f"{SAVE_FOLDER}leaders.json"
}

def save_id_counters():
    id_counter_dict = {
        "dep_id_counter": Department.get_counter(),
        "team_id_counter": Team.get_counter(),
        "job_id_counter": JobPosition.get_counter(),
        "worker_id_counter": Worker.get_counter(),
        "manager_id_counter": Manager.get_counter(),
        "leader_id_counter": Leader.get_counter()
    }
    with open(ID_COUNTER_FILE, "w") as f:
        json.dump(id_counter_dict, f, indent=4)


def save_repository_to_files():
    save_id_counters()
    for key, value in FILES.items():
        object_list = getattr(Repository, key)
        list_of_dicts = Repository.make_list_of_dicts(object_list)
        with open(value, "w") as f:
            json.dump(list_of_dicts, f, indent=4)

def load_data(filename:str):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"File '{filename}' was not found!")

def load_repository_from_files():
    DEPARTMENTS = {}
    TEAMS = {}
    JOBS = {}
    WORKERS = {}
    MANAGERS = {}
    LEADERS = {}
    # 1) Load raw JSON dictionaries
    deps_data = load_data(FILES["departments"])
    teams_data = load_data(FILES["teams"])
    jobs_data = load_data(FILES["jobs"])
    workers_data = load_data(FILES["workers"])
    managers_data = load_data(FILES["managers"])
    leaders_data = load_data(FILES["leaders"])
    id_counters = load_data(ID_COUNTER_FILE)
    
    # 2) Create class instances without references
    if deps_data:
        for dep in deps_data:
            temp_dep = Department(dep["name"])
            temp_dep.id = dep["id"]
            DEPARTMENTS[dep["id"]] = temp_dep

    if teams_data:
        for team in teams_data:
            temp_team = Team(team["name"])
            temp_team.id = team["id"]
            TEAMS[team["id"]] = temp_team

    if jobs_data:
        for job in jobs_data:
            temp_job = JobPosition(job["name"], job["level"])
            temp_job.id = job["id"]
            JOBS[job["id"]] = temp_job

    if workers_data:
        for worker in workers_data:
            temp_worker = Worker(worker["name"], worker["surname"], worker["salary"])
            temp_worker.id = worker["id"]
            WORKERS[worker["id"]] = temp_worker

    if managers_data:
        for manager in managers_data:
            temp_manager = Manager(manager["name"], manager["surname"], manager["salary"])
            temp_manager.id = manager["id"]
            MANAGERS[manager["id"]] = temp_manager

    if leaders_data:
        for leader in leaders_data:
            temp_leader = Leader(leader["name"], leader["surname"], leader["salary"])
            temp_leader.id = leader["id"]
            LEADERS[leader["id"]] = temp_leader

    # 3) Update ID counters
    if id_counters:
        for key, value in id_counters.items():
            if key == "dep_id_counter":
                Department.set_counter(value)
            if key == "team_id_counter":
                Team.set_counter(value)
            if key == "job_id_counter":
                JobPosition.set_counter(value)
            if key == "worker_id_counter":
                Worker.set_counter(value)
            if key == "manager_id_counter":
                Manager.set_counter(value)
            if key == "leader_id_counter":
                Leader.set_counter(value)

    # 4) Resolve references
    if deps_data:
        for dep_dict in deps_data:
            dep = DEPARTMENTS[dep_dict["id"]]
            dep.manager = MANAGERS.get(dep_dict["manager"])
            dep.teams = [TEAMS[t_id] for t_id in dep_dict["teams"]]
            dep.members = [WORKERS[w_id] for w_id in dep_dict["members"]]
            dep.jobs = [JOBS[j_id] for j_id in dep_dict["jobs"]]
    if teams_data:
        for team_dict in teams_data:
            team = TEAMS[team_dict["id"]]
            team.department = DEPARTMENTS.get(team_dict["department"])
            team.members = [WORKERS[w_id] for w_id in team_dict["members"]]

    if jobs_data:
        for job_dict in jobs_data:
            job = JOBS[job_dict["id"]]
            job.department = DEPARTMENTS.get(job_dict["department"])

    if workers_data:
        for worker_dict in workers_data:
            worker = WORKERS[worker_dict["id"]]
            worker.job = JOBS.get(worker_dict["job"])

    if managers_data:
        for manager_dict in managers_data:
            manager = MANAGERS[manager_dict["id"]]
            manager.department = DEPARTMENTS.get(manager_dict["department"])

    if leaders_data:
        for leader_dict in leaders_data:
            leader = LEADERS[leader_dict["id"]]
            leader.departments = [DEPARTMENTS[d_id] for d_id in leader_dict["departments"]]    

