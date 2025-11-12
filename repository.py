from data_objects import (
    Department, 
    Team, 
    JobPosition, 
    Worker, 
    Manager, 
    Leader
)    

class Repository:
    departments = []
    teams = []
    jobs = []
    workers = []
    managers = []
    leaders = []

    @staticmethod
    def auto_id(proper_list:list):
        return str(len(proper_list)+1)

    @staticmethod
    def make_list_of_dicts(list_of_instances:list):
        return [instance.get_dict() for instance in list_of_instances]

    @classmethod
    def add(cls, obj):
        if isinstance(obj, Department):
            obj.id = "D"+cls.auto_id(cls.departments)
            cls.departments.append(obj)
        elif isinstance(obj, Team):
            obj.id = "T"+cls.auto_id(cls.teams)
            cls.teams.append(obj)
        elif isinstance(obj, JobPosition):
            obj.id = "J"+cls.auto_id(cls.jobs)
            cls.jobs.append(obj)
        elif isinstance(obj, Worker):
            obj.id = "W"+cls.auto_id(cls.workers)
            cls.workers.append(obj)
        elif isinstance(obj, Manager):
            obj.id = "M"+cls.auto_id(cls.managers)
            cls.managers.append(obj)
        elif isinstance(obj, Leader):
            obj.id = "L"+cls.auto_id(cls.leaders)
            cls.leaders.append(obj)