# 등급에 따른 과목평점 변환 함수
def convert(a):
    if a == 'A+':
        a = 4.5
    elif a == 'A0':
        a = 4.0
    elif a == 'B+':
        a = 3.5
    elif a == 'B0':
        a = 3.0
    elif a == 'C+':
        a = 2.5
    elif a == 'C0':
        a = 2.0
    elif a == 'D+':
        a = 1.5
    elif a == 'D0':
        a = 1.0
    elif a == 'F':
        a = 0.0
    elif a == 'P':
        a = 0.0
    return a

sum = 0
creditSum = 0

for _ in range(20):
    name, credit, grade = map(str, input().split())
    # P 과목 계산에서 제외
    if grade == 'P':
        pass
    else:
        sum += float(credit)*float(convert(grade))
        creditSum += float(credit)

print(sum/creditSum)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total_gpa = 0
total_grade = 0
for _ in range(20):
    subject, gpa, grade = input().split()
    gpa = float(gpa)        # 실수형으로 만들어준다 int 사용x b/c 예제에 3.0등으로 이루어짐
    if grade != 'p':
        total_gpa += gpa
        total_grade += gpa * grade_list[rating.index(grade)]   # 학점 * 과목평점

print('%.6f' % (total_grade / total_gpa))
