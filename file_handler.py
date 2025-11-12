import json
from repository import Repository
from data_objects import (
    Department, 
    Team, 
    JobPosition, 
    Worker, 
    Manager, 
    Leader
)

SAVE_FOLDER = "Data Files/"

FILES = {
"departments": f"{SAVE_FOLDER}departments.json",
"teams": f"{SAVE_FOLDER}teams.json",
"jobs": f"{SAVE_FOLDER}jobs.json",
"workers": f"{SAVE_FOLDER}workers.json",
"managers": f"{SAVE_FOLDER}managers.json",
"leaders": f"{SAVE_FOLDER}leaders.json"
}

def save_repository_to_files():
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
    # 1) Load raw JSON dictionaries
    """deps_data = load_data(FILES["departments"])
    teams_data = load_data(FILES["teams"])
    jobs_data = load_data(FILES["jobs"])
    workers_data = load_data(FILES["workers"])
    managers_data = load_data(FILES["managers"])
    leaders_data = load_data(FILES["leaders"])"""
    data = {}
    for key, value in FILES.items():
        data[key] = load_data(value)
    print(data)

    # 2) Create objects without references
    for key, value in data.items():
        if value:
            for record in value:
                if key == "departments":
                    Department(record["name"])
                if key == "teams":
                    Team(record["name"])
                if key == "jobs":
                    JobPosition(record["name"], record["level"])
                if key == "workers":
                    Worker(record["name"], record["surname"], record["salary"])
                if key == "managers":
                    Manager(record["name"], record["surname"], record["salary"])
                if key == "leaders":
                    Leader(record["name"], record["surname"], record["salary"])

    # 3) Resolve references

    
def resolve_references():
    pass

def save_data(filename:str, list_of_dicts:list):
    with open(filename, "w") as f:
        json.dump(list_of_dicts, f, indent=4)


if __name__ == "__main__":
    load_repository_from_files()
    print()
    for dep in Repository.departments:
        print(dep)
