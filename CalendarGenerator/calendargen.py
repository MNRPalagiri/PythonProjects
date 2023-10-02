import calendar as cal
from datetime import date,datetime
import pandas as pd
import openpyxl as xl


def numberofdaysinamonth(curryear,currmonth):
    return cal.monthrange(curryear,currmonth)[1]

def getnumberofdaysofyear(curryear):
    return 365+cal.isleap(curryear)

def getweekdays(curryear):
   
    day = datetime.weekday(date(curryear,1,1))

    switcher={
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
    }

    days =[]
    days.append("")

    for x in range(getnumberofdaysofyear(curryear)):
        days.append(switcher.get(day,"nothing"))
        day+=1
        if day==7:
            day=0

    return days    
        
def getcaldays(curryear):
    firstrow=[]
    firstrow.append("")
    for x in range(12):
        numberofdaysincurrMonth = numberofdaysinamonth(curryear,x+1)
        for day in range(numberofdaysincurrMonth):
            firstrow.append(day+1)

    return firstrow    






curryear =date.today().year

weekdaylist  = getweekdays(curryear)

currDataFrame = pd.DataFrame(columns=weekdaylist)
currDataFrame.loc[len(currDataFrame.index)] = getcaldays(curryear)

currDataFrame.to_csv("./test.csv")
currDataFrame.to_excel(excel_writer="./Calendar.xlsx" ,sheet_name="Calendar")