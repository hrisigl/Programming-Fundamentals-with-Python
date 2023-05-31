import math

first_emp = int(input())
second_emp = int(input())
third_emp = int(input())
students_count = int(input())

questions_per_hour = first_emp + second_emp + third_emp
needed_hours = math.ceil(students_count / questions_per_hour)

for hour in range(1, needed_hours + 1):
    students_count -= questions_per_hour
    if students_count <= 0:
        break
    if hour % 3 == 0:
        needed_hours += 1

print(f"Time needed: {needed_hours}h.")
