student_grades = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    student_grades.append([name,score])

student_grades.sort(key=lambda x: x[1])
low_grade = student_grades[0][1]
second_low_grade = None
result = []
for s in [x for x in student_grades if x[1] > low_grade]:
    if not second_low_grade:
        second_low_grade = s[1]
        result.append(s[0])
    else:
        if s[1] == second_low_grade:
            result.append(s[0])
        else:
            break

result.sort()

for n in result:
    print(n)
