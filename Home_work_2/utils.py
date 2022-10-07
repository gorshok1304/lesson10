import functions

print("введите номер студента")
student_id = int(input())
student = functions.get_student_by_pk(student_id)

if not student:
    print("у нвс нет такого студента")
    quit()

student_name = student["full_name"]
student_skills = " ".join(student["skills"])
student_learns = " ".join(student["learns"])

print(f"студент {student_name}")
print(f"знает {student_skills}")

print(f"выберите специальность для оценки студента {student_name}")
profession_title = input()
profession = functions.get_profession_by_title(profession_title)

if not profession:
    print("у нас нет такой профессии")
    quit()

fitness = functions.check_fitness(student, profession)

fit_percent = fitness["fit_percent"]
has = fitness["has"]
lacks = fitness["lacks"]

print(f"пригодность {fit_percent}%")
print(f"студент знает {' '.join(has)}")
print(f"студент не знает {' '.join(lacks)}")
