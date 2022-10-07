import json

from config import STUDENTS_PATH, PROFESSIONS_PATH

def load_students():
    with open(STUDENTS_PATH, "r", encoding="utf-8") as file:
        stud = json.load(file)
        return stud


def load_professions():
    with open(PROFESSIONS_PATH, "r", encoding="utf-8") as file:
        prof = json.load(file)
    return prof


def get_student_by_pk(pk):
    students = load_students()
    for student in students:
        if student.get("pk") == pk:
            return student


def get_profession_by_title(title):
    professions = load_professions()
    for profession in professions:
        if profession.get("title") == title.title():
            return profession


def check_fitness(student, profession):


    student_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    has_skills = student_skills.intersection(profession_skills)
    lacks_skills = profession_skills.difference(has_skills)

    has_percent = round(len(has_skills)) / len(profession_skills)

    return {
        "has": list(has_skills),
        "lacks": list(lacks_skills),
        "fit_percent": has_percent
    }



