def  have_yen(n,m):   #定义一个方法
     n=n+m            
     return n         
num=int(input("请输入一个值："))  
num1=int(input("请输入一个数："))  
num2=have_yen(num,num1)    #获取这个方法的返回值
print(num2)                #输出此方法的返回值
