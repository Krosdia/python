e1 = {'name':'Jack', 'age':22, 'sal':8000}
e2 = {'name':'Tom', 'age':27, 'sal':5000}
e3 = {'name':'Nick', 'age':26, 'sal':8000}
e4 = {'name':'Mary', 'age':21, 'sal':12000}
e5 = {'name':'Lucy', 'age':22, 'sal':3000}
e = [e1, e2, e3, e4, e5]

while True:
    print ("1. 添加员工信息")
    print ("2. 输出员工信息")
    print ("3. 退出程序")
    option = input('请选择[1-->3]: ')
    if option == '1':
        name = input('请输入员工名字:')
        age = input('请输入员工年龄:')
        salary = input('请输入员工工资:')
        e.append({'name':name, 'age':age, 'sal': salary})
        print ("添加员工信息成功\n")

    elif option == '2':
        for i in range(1,5):
            
    elif option == '3':
        break
    else:
        print ("错误选项")


