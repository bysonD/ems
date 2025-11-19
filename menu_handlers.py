from loop_handler import *
from menu_methods_handler import *
from menu_texts import *
from repository import Repository

def main_menu():
    default_menu_loop(main_menu_desc(), {
        1: lambda: section_menu("leader"),
        2: lambda: section_menu("department"),
        3: lambda: section_menu("manager"),
        4: lambda: section_menu("worker"),
        5: lambda: section_menu("team"),
        6: lambda: section_menu("job"),
        0: None
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
        handlers[1] = create_team
        handlers[2] = create_job
    if cls_type == "Team":
        handlers[1] = add_member_to_team
    if cls_type == "Manager":
        handlers[1] = create_worker
        handlers[2] = change_salary_of_worker
    if cls_type == "Leader":
        handlers[1] = create_department
        handlers[2] = set_new_manager
        handlers[3] = change_salary_of_manager
    handlers[0] = None
    default_menu_loop(instance_menu_desc(instance), handlers, lambda: print(instance))

def choose_from_instances():
    pass

def create_instance_menu(creator, creating:str):
    handlers = {}
    default_menu_loop(instance_creation_menu_text(creator.get_name(), creating), handlers)
