def fun1(n):
    print('判断传入对象的长度')
    if len(n) >= 0: 
        return len(n)
    else:
        return False
content = input('Please enter some content:')
print(fun1(content))
