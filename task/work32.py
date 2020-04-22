import datetime
class student:
    def __init__(self,Sno,Sname,Sbarthday,Sfaction):
        self.Sage = 0
        self.Sgarde = '优秀'
        self.Sname = Sname
        self.Sno = Sno
        self.Sbarthday = datetime.datetime.strptime(Sbarthday,"%Y-%m-%d")
        self.Sfaction = Sfaction
        self.Setage(Sbarthday)
        self.SetGarde(Sfaction)
        def Setage(self,Sbarthday):
            if (datetime.date.today().month - self.Sbarthday.month)>=0:
                if (datetime.date.today().day - self.Sbarthday.day)<0 & (datetime.date.today().month - self.Sbarthday.month)==0:
                    self.Sage = datetime.date.today().year - self.Sbarthday.year -1
                    else:
                    self.Sage = datetime.date.today().year - self.Sbarthday.year
                    else:
                    self.Sage = datetime.date.today().year - self.Sbarthday.year -1
        def SetGarde(self,Sfaction):
            if self.Sfaction >= 80:
                self.Sgarde = '优秀'
            elif self.Sfaction >= 70 & self.Sfaction <80:
                self.Sgarde = '良好'
            elif self.Sfaction >= 60 & self.Sfaction <70:
                self.Sgarde = '及格e799bee5baa6e997aee7ad94e58685e5aeb931333431373332'
            else:
            self.Sgarde = '不及格'

text1 = student('2018061','张三','1999-10-27',68)
print("学号：{0} 姓名：{1} 年龄：{2} 分数：{3} 等级：{4}".format(text1.Sno,text1.Sname,text1.Sage,text1.Sfaction,text1.Sgarde)) 