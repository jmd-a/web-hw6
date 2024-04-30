from faker import Faker
import random
import sqlite3
from datetime import datetime

fake = Faker()

conn = sqlite3.connect('university.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                group_id INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY,
                name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY,
                name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY,
                name TEXT,
                teacher_id INTEGER)''')

c.execute('''CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject_id INTEGER,
                grade INTEGER,
                date DATE)''')

for i in range(1, 4):
    c.execute("INSERT INTO groups (name) VALUES (?)", (f'Group {i}',))

for i in range(30):
    name = fake.name()
    group_id = random.randint(1, 3)
    c.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

for i in range(1, 6):
    name = fake.name()
    c.execute("INSERT INTO teachers (name) VALUES (?)", (name,))

for i in range(5, 9):
    teacher_id = random.randint(1, 5)
    c.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (f'Subject {i}', teacher_id))

for student_id in range(1, 31):
    for subject_id in range(1, 9):
        grade = random.randint(1, 100)
        date = fake.date_between(start_date='-1y', end_date='today').isoformat()
        c.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                  (student_id, subject_id, grade, date))

conn.commit()
conn.close()