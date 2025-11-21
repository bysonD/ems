from controllers.loop_handler import *
from controllers.menu_methods_handler import *
from helpers.menu_texts import *
from file_handler import load_repository_from_files
from pathlib import Path
from models.logger import LOG_FOLDER_NAME


def main_menu():
    load_repository_from_files()
    default_menu_loop(main_menu_desc(), {
        1: lambda: section_menu("leader"),
        2: lambda: section_menu("department"),
        3: lambda: section_menu("manager"),
        4: lambda: section_menu("worker"),
        5: lambda: section_menu("team"),
        6: lambda: section_menu("job"),
        7: describe_company,
        8: logs_loop,
        9: import_starter_method,
        0: save_and_exit
    })

def section_menu(class_name:str):
    """Acceptable class names: department || team || job || worker || manager || leader"""
    handlers = {}
    handlers[1] = lambda: listing_menu(class_name+"s")
    if class_name == "leader":
        handlers[2] = create_leader
    if class_name == "manager":
        handlers[2] = create_manager
    handlers[0] = None
    default_menu_loop(base_listing_menu_desc(class_name), handlers)

def listing_menu(list_name:str):
    """List names: departments || teams || jobs || workers || managers || leaders"""
    selected_list = getattr(Repository, list_name)
    list_ids = get_list_ids(selected_list)

    handlers = {}

    for index, item_id in enumerate(list_ids, start=1):
        instance = get_instance_by_id(item_id, selected_list)

        handlers[index] = lambda inst=instance: instance_menu(inst)

    handlers[0] = None
    default_menu_loop(list_hint(selected_list), handlers, lambda: list_instances(selected_list))

def instance_menu(instance):
    cls_type = instance.__class__.__name__
    handlers = {}
    if cls_type == "Department":
        handlers[1] = lambda: create_team(instance)
        handlers[2] = lambda: create_job(instance)
    if cls_type == "Team":
        handlers[1] = add_member_to_team(instance)
    if cls_type == "Manager":
        handlers[1] = lambda: create_worker(instance)
        handlers[2] = lambda: change_salary_of_worker(instance)
    if cls_type == "Leader":
        handlers[1] = lambda: create_department(instance)
        handlers[2] = lambda: set_new_manager(instance)
        handlers[3] = lambda: change_salary_of_manager(instance)
    handlers[0] = None
    default_menu_loop(instance_menu_desc(instance), handlers, lambda: print(instance))

def describe_company():
    default_menu_loop(company_structure_description(), {0: None})

def logs_loop():
    log_folder = Path(LOG_FOLDER_NAME)
    log_files = [f for f in log_folder.iterdir() if f.is_file()]
    logs_text = "Available logs\n"

    handlers = {}
    for i in range(len(log_files)):
        handlers[i+1] = lambda lf=log_files[i]: load_log(lf)
        logs_text += f"\n{i+1}. {log_files[i].name}"
    handlers[0] = None
    default_menu_loop(logs_text, handlers)
