from data_objects import Department, Team, JobPosition, Worker, Manager, Leader

def starter():
    job_levels = JobPosition.levels

    dep_1 = Department("IT")
    dep_2 = Department("Marketing")
    dep_3 = Department("Finance")

    team_1 = Team("DevOps", dep_1)
    team_2 = Team("Graphic Designers", dep_2)
    team_3 = Team("Economists", dep_3)

    job_1 = JobPosition("Programmer", job_levels[0], dep_1)
    job_2 = JobPosition("Vector Artist", job_levels[1], dep_2)
    job_3 = JobPosition("Accountant", job_levels[2], dep_3)

    worker_1 = Worker("John", "Snow", 1500, job_1)
    worker_2 = Worker("Mark", "Twain", 2200, job_2)
    worker_3 = Worker("Joe", "Mama", 3000, job_3)
    worker_11 = Worker("Jimmy", "Clarks", 2200, job_1)
    worker_22 = Worker("Jon", "Jones", 2300, job_2)
    worker_33 = Worker("Yann", "O'Schick", 3500, job_3)

    man_1 = Manager("Alex", "The Great", 4000)
    man_2 = Manager("Ronald", "Brown", 3500)
    man_3 = Manager("Dan", "Collins", 4200)

    leader = Leader("Peter", "Griffins", 6000)

    team_1.add_to_team(worker_1)
    team_1.add_to_team(worker_11)
    team_2.add_to_team(worker_2)
    team_2.add_to_team(worker_22)
    team_3.add_to_team(worker_3)
    team_3.add_to_team(worker_33)

    leader.add_departments(dep_1, dep_2, dep_3)

    leader.set_manager(dep_1, man_1)
    leader.set_manager(dep_2, man_2)
    leader.set_manager(dep_3, man_3)
