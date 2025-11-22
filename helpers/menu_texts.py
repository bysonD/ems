from helpers.global_utils import SEPARATOR_MULTIPLIER

def department_menu_desc(name:str):
    return f"""DEPARTMENT: {name}
----------------------------
1. Create a new team
2. Create a new job position
"""

def team_menu_desc(name:str):
    return f"""TEAM: {name}
----------------------------
1. Add a member to the team
"""

def manager_menu_desc(name:str):
    return f"""MANAGER: {name}
--------------------------------
1. Hire a new worker
2. Change the salary of a worker
"""

def leader_menu_desc(name:str):
    return f"""LEADER: {name}
------------------------------------
1. Create a new department
2. Set a new manager of a department
3. Change the salary of a manager
"""

def main_menu_desc():
    return f"""EMS - Employee Managment System
{"-" * SEPARATOR_MULTIPLIER}
1. Leaders
2. Departments
3. Managers
4. Workers
5. Teams
6. Jobs
{"-" * SEPARATOR_MULTIPLIER}
7. Company structure
8. View logs
9. Import starter method
{"-" * SEPARATOR_MULTIPLIER}
0. Save and exit
"""

def base_listing_menu_desc(section_name: str):
    header = f"{section_name.upper()}S MENU\n{"-"*SEPARATOR_MULTIPLIER}\n"

    if section_name == "manager":
        body = f"1. List all {section_name}s\n2. Create a new {section_name}\n"
    elif section_name == "leader":
        body = f"1. List all {section_name}s\n"
    else:
        body = f"1. List all {section_name}s\n"
    
    return header + body

def instance_menu_desc(instance):
    """instance - instance of these classes: Department, Team, JobPosition, Worker, Manager, Leader"""
    inst_name = instance.get_name()
    class_type = instance.__class__.__name__
    header = f"\nMENU FOR: {class_type} {inst_name}\n"

    if class_type == "Department":
        body = f"""{"-"*SEPARATOR_MULTIPLIER}
1. Create a new team
2. Create a new job position"""
    elif class_type == "Team":
        body = f"""{"-"*SEPARATOR_MULTIPLIER}
1. Add a member to the team"""
    elif class_type == "JobPosition":
        body = ""
    elif class_type == "Worker":
        body = ""
    elif class_type == "Manager":
        body = f"""{"-"*SEPARATOR_MULTIPLIER}
1. Hire a new worker
2. Change the salary of a worker"""
    elif class_type == "Leader":
        body = f"""{"-"*SEPARATOR_MULTIPLIER}
1. Create a new department
2. Hire a new manager
3. Set a new manager of a department
4. Change the salary of a manager"""
    else:
        body = "Uknown class type!"

    body += "\n"+"-"*SEPARATOR_MULTIPLIER
    return header+body

def starter_menu():
    return f"""1. Import starting data
2. Do NOT import starting data"""
