import random
list =[]
for i in range(1,20):
    grade = random.randint(1,100)
    list.append(grade)
if grade > 89:
    print('成绩等级：', 'A')
elif grade > 79:
    print('成绩等级：', 'B')
elif grade > 69:
    print('成绩等级：', 'C')
elif grade >59:
    print('成绩等级：', 'D')
else:
    print('成绩等级：', 'E')
