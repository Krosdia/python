#coding=utf-8
import calendar
import time
def getday(year_m_d):
    try:
        year,month,day = map(int,year_m_d.split('.'))
        time.strptime('%s%s%s'%(year,month,day), "%Y%m%d")
        all_days=0
        for i in range(1,month):
            all_days = calendar.monthrange(year,i)[1]+all_days
        return all_days+day
    except Exception,e:
        print e
        return None
year_m_d='2001.05.07'
print getday(year_m_d)