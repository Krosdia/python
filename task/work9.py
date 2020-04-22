print("猜数字游戏")
print("请输入一个数字：")
a = input()
b = a *5
i = 0
print("输入猜数字次数：") 
c=int(input())
while i < c:
    print("请输入要猜的数字：")
    d = input()
    if(d == b):
        print("猜中了")
    else:
        print("未猜中")
    i+=1
