import sqlite3

COMPANY = "company.db"
DEPARTMENTS = "departments"
TEAMS = "teams"
JOBS = "jobs"
WORKERS = "workers"
MANAGERS = "managers"
LEADERS = "leaders"

def initialize_db():
    return sqlite3.connect(COMPANY)

def initialize_cursor(connected_db):
    return connected_db.cursor()

def create_tables():
    conn = initialize_db()
    cursor = initialize_cursor(conn)

    leaders_query = f"""CREATE TABLE IF NOT EXISTS {LEADERS} (
    leader_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    salary INTEGER NOT NULL);
"""

    departments_query = f"""CREATE TABLE IF NOT EXISTS {DEPARTMENTS} (
    dep_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NUT NULL,
    leader_id INTEGER UNIQUE,
    FOREIGN KEY (leader_id) REFERENCES {LEADERS}(leader_id));
"""
    teams_query = f"""CREATE TABLE IF NOT EXISTS {TEAMS} (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    dep_id INTEGER UNIQUE,
    FOREIGN KEY (dep_id) REFERENCES {DEPARTMENTS}(dep_id));
"""
    jobs_query = f"""CREATE TABLE IF NOT EXISTS {JOBS} (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    level TEXT NOT NULL,
    name TEXT NOT NULL,
    dep_id INTEGER UNIQUE,
    FOREIGN KEY (dep_id) REFERENCES {DEPARTMENTS}(dep_id));
"""
    workers_query = f"""CREATE TABLE IF NOT EXISTS {WORKERS} (
    worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    salary INTEGER NOT NULL,
    team_id INTEGER UNIQUE,
    dep_id INTEGER UNIQUE,
    FOREIGN KEY (team_id) REFERENCES {TEAMS}(team_id),
    FOREIGN KEY (dep_id) REFERENCES {DEPARTMENTS}(dep_id));
"""
    managers_query = f"""CREATE TABLE IF NOT EXISTS {MANAGERS} (
    manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    salary INTEGER NOT NULL,
    dep_id INTEGER UNIQUE,
    FOREIGN KEY (dep_id) REFERENCES {DEPARTMENTS}(dep_id));
"""
    list_of_queries = [leaders_query, departments_query, teams_query, jobs_query, workers_query, managers_query]

    for query in list_of_queries:
        cursor.execute(query)

create_tables()