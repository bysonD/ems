import os

SEPARATOR_MULTIPLIER = 50

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def warning_out_of_range(min:int, max:int):
    return f"""{"/"*SEPARATOR_MULTIPLIER}
Invalid input, choose a number between {min} and {max}!
{"/"*SEPARATOR_MULTIPLIER}"""

def default_warning():
        return f"""{"/"*SEPARATOR_MULTIPLIER}
Invalid input, try again!
{"/"*SEPARATOR_MULTIPLIER}"""

def not_in_list_warning(proper_list:list):
    return f"""{"/"*SEPARATOR_MULTIPLIER}
Invalid input, choose a value from {proper_list}!
{"/"*SEPARATOR_MULTIPLIER}"""

def input_message(max_input:int = None):
    if max_input:
        return f"Select [1 to {max_input}] OR type [0] to exit: "
    else:
        return f"Type [0] to exit: "
    
def list_hint(instance_list:list):
    """
    input_list - needs to be a list of class instances
    Acceptable classes: Department, Team, JobPosition, Worker, Manager, Leader
    """
    if instance_list:
        result = "AVAILABLE OPTIONS\n"
        for i in range(len(instance_list)):
            result += f"\n{i+1}. [{instance_list[i].introduce()}]"

        result += f"\n{"-"*SEPARATOR_MULTIPLIER}"
    else:
        result = "NO AVAILABLE OPTIONS\n"
    return result

def base_list_hint(base_list:list):
    if base_list:
        result = "\nAVAILABLE OPTIONS\n"
        for i in range(len(base_list)):
            result +=f"\n{i+1}. {base_list[i]}"
        result += f"\n{"-"*SEPARATOR_MULTIPLIER}"
    else:
        result = "\nNO AVAILABLE OPTIONS\n"
    return result

def company_structure_description():
    return f"""COMPANY STRUCTURE
{"-"*SEPARATOR_MULTIPLIER}
LEADERS
    - Can create new departments
    - Can change salary of managers
    - Can set a new manager to an existing department
{"/"*SEPARATOR_MULTIPLIER}
DEPARTMENTS
    - Can create teams
    - Can create job positions
{"/"*SEPARATOR_MULTIPLIER}
MANAGERS
    - Can hire new workers
    - Can change salary of an existing worker
{"/"*SEPARATOR_MULTIPLIER}
TEAMS
    - Can add workers to themselves
{"/"*SEPARATOR_MULTIPLIER}
WORKERS & JOB POSITIONS
    - Can be listed
{"/"*SEPARATOR_MULTIPLIER}"""
