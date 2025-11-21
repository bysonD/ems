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
    def make_list_of_dicts(list_of_instances:list):
        return [instance.get_dict() for instance in list_of_instances]

    @classmethod
    def add(cls, obj):
        if isinstance(obj, Department):
            cls.departments.append(obj)
        elif isinstance(obj, Team):
            cls.teams.append(obj)
        elif isinstance(obj, JobPosition):
            cls.jobs.append(obj)
        elif isinstance(obj, Worker):
            cls.workers.append(obj)
        elif isinstance(obj, Manager):
            cls.managers.append(obj)
        elif isinstance(obj, Leader):
            cls.leaders.append(obj)
            