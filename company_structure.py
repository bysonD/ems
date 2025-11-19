def company_structure_description():
    separator_multiplier = 60
    return f"""COMPANY STRUCTURE
{"-"*separator_multiplier}
LEADERS
    - Can create new departments
    - Can change salary of managers
    - Can set a new manager to an existing department
{"/"*separator_multiplier}
DEPARTMENTS
    - Can create teams
    - Can create job positions
{"/"*separator_multiplier}
MANAGERS
    - Can hire new workers
    - Can change salary of an existing worker
{"/"*separator_multiplier}
TEAMS
    - Can add workers to themselves
{"/"*separator_multiplier}
WORKERS & JOB POSITIONS
    - Can be listed
{"/"*separator_multiplier}"""
