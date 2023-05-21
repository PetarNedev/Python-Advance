
number_of_students = int(input())

students_grade = {}

for _ in range(number_of_students):
    name, grade = tuple(input().split())
    grade = float(grade)

    if name not in students_grade:
        students_grade[name] = []
    students_grade[name].append(grade)

for name, grade in students_grade.items():
    avg = sum(grade) / len(grade)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grade])} (avg: {avg:.2f})")
