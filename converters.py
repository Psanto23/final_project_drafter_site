def convert_date_to_num(date:str):
    date = date.split("-")
    year = date[0]
    year = int(year[2:])
    day = int(date[2])
    month = int(date[1])
    #the math formula: (year + year/4 + day - 1 (if leap year or Jan or Feb) + month constant) mod 7
    y = year//4
    if(month <= 2 or year/4 == 0):
        y = y-1
    y = y+day+year
    print(y)
    if(month == 1 or month == 10):
        y = y+6
    if(month == 2 or month == 3 or month == 11):
        y = y+2
    if(month == 4 or month == 7):
        y = y+5
    if(month == 6):
        y = y+3
    if(month == 8):
        y = y+1
    if(month == 9 or month == 12):
        y = y+4

    return y%7

def convert_time_to_num(time:str)->int:
    if(time == ""):
        return 0
    times = time.split(":")
    hours = int(times[0])
    split = times[1]
    minutes = int(split[0:2])
    am_pm = split[2:]
    if(hours == 12):
        hours = 0
    if(am_pm == "PM"):
        hours = hours + 12 
    
    return hours*100 + minutes
    
def convert_day(day:str)->int:
    if(day == "Sun"):
        return 1
    if(day == "Mon"):
        return 2
    if(day == "Tue"):
        return 3
    if(day == "Wed"):
        return 4
    if(day == "Thu"):
        return 5
    if(day == "Fri"):
        return 6
    if(day == "Sat"):
        return 7
    
def find_start(time:str, times:list)->int:
    count = 0
    for t in times:
        if(time != t):
            count = count+1
        else:
            return count
    return 0


