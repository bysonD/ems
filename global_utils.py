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

def input_message(max_input:int):
    if max_input:
        return f"Select [1 to {max_input}] OR press [0] to exit: "
    else:
        return f"-- Press [0] to exit --"
    
def list_hint(input_list:list):
    """
    input_list - needs to be a list of class instances
    Acceptable classes: Department, Team, JobPosition, Worker, Manager, Leader
    """
    result = ""
    for i in range(len(input_list)):
        result += f"\n{i+1}. [{input_list[i].introduce()}]"

    result += f"\n{"-"*SEPARATOR_MULTIPLIER}"
    return result

def id_input_message(ids_list:list):
    return f"Select an ID from {ids_list} OR press [0] to exit: "
    
