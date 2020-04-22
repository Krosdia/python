
list = []

def the_input (count=eval(input("输入乘数的总个数："))):
    for  i  in range(count):
        n=eval(input("依次输入相乘数"))
        list.append(n)
        print("相乘数列表：",list)
the_input()
def product(*args):
       sum =1
       for n in args:
           sum =sum * n
       return sum
print("最终结果：",product(*list))
