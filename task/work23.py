dict={}
class student(object):
    def __init__(self,number,name):
        self.name=name
        self.number=number
    def Dict(self):
        dict[self.number]=self.name
def Student(number,name):
    a = student(number,name).Dict()
def sort():
    test=[]
    for i in dict:
        test.append(i)
    test.sort()
    for i in test:
        print(i,dict[i])
 
Student('3','T1')
Student('2','T2')
Student('1','T3')
Student('4','T4')
print(dict)
sort()