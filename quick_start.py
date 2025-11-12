from data_objects import Department, Team, JobPosition, Worker, Manager, Leader

def start():
    dep = Department("Marketing")
    dep2 = Department("IT")

    team = Team("AJtaci", dep2)
    team2 = Team("Posuci", dep2)
    team3 = Team("Bohove Olympu", dep)

    job = JobPosition("Backender", JobPosition.levels[1], dep2)
    job1 = JobPosition("Kameraman", JobPosition.levels[0], dep)
    job2 = JobPosition("Grafik", JobPosition.levels[2], dep)

    work1 = Worker("Janko", "Hrasko", 2500, job)
    work2 = Worker("Denis", "Dunaj", 1500, job1)
    work1 = Worker("Ivan", "Tonaj", 4000, job2)

    man = Manager("Miky", "Mora", 5000, dep)
    man2 = Manager("Roman","Janov", 4800, dep2)

    lead = Leader("Pet", "Postar", 6000)