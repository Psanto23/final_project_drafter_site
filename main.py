from drafter import *
from converters import *
from dataclasses import dataclass
from datetime import date



@dataclass
class Event:
    name:str
    day: str
    start_time: str
    duration: float
    
@dataclass
class State:
    schedule: list[Event]
    start_time:str
    end_time:str
    start_date:str
    start_day: int
    r:int
    g:int
    b:int
    error:str
    


DAYS = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
        "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
HOURS = [
    '12:00AM', '12:30AM', '1:00AM', '1:30AM', '2:00AM', '2:30AM',
    '3:00AM', '3:30AM', '4:00AM', '4:30AM', '5:00AM', '5:30AM',
    '6:00AM', '6:30AM', '7:00AM', '7:30AM', '8:00AM', '8:30AM',
    '9:00AM', '9:30AM', '10:00AM', '10:30AM', '11:00AM', '11:30AM',
    '12:00PM', '12:30PM', '1:00PM', '1:30PM', '2:00PM', '2:30PM',
    '3:00PM', '3:30PM', '4:00PM', '4:30PM', '5:00PM', '5:30PM',
    '6:00PM', '6:30PM', '7:00PM', '7:30PM', '8:00PM', '8:30PM',
    '9:00PM', '9:30PM', '10:00PM', '10:30PM', '11:00PM', '11:30PM'
]


@route
def index(state:State)->Page:
    '''
    this is the main page of the site where
    you can see and make your schedule and
    access all the other pages
    '''
    #css
    add_website_css(
    "table",
    f"background-color: rgb({state.r}, {state.g}, {state.b});")
    #creation of table
    rows = []
    day_times = []
    day_range = ((convert_time_to_num(state.end_time) - convert_time_to_num(state.start_time))//50)+1
    start = find_start(state.start_time, HOURS)
    for i in range(start,start+day_range):
        day_times.append(HOURS[i])
    for hour in day_times:
        rows.append([hour] + [""] * 7)
    #where events are added
    if(state.schedule != []):  
        for event in state.schedule:
            x = (int(event.start_time[0:1])*60 + (int(event.start_time[2:4]) - (6*60)))//30
            y = convert_day(event.day) - convert_day(DAYS[state.start_day])
            if(y<0):
                y*-1
            for i in range(int(event.duration//.5)):
                rows[x][y+1] = event.name
                x= x+1
        
    return Page(state, [
        Text(state.error),
        Header("Schedulizer"),
        "Starting Week: ",
        DateInput("day", state.start_date, on_change="change_date"),
        "\n",
        Button("Add Event+", "event_form"),
        Button("Remove Event-", "remove_form"),
        Button("Customize", "customize_form"),
        Table(rows, ["Time"] + DAYS[state.start_day:state.start_day+7]),
        ])

@route
def change_date(state: State, day: str)-> Page:
    '''
    Updates the date and moves the week to the
    correct day accordingly
    '''
    state.start_day = convert_date_to_num(day)
    state.start_date = day
    return index(state)


#adds event
@route
def event_form(state: State)-> Page:
    '''
    A page that allows the user
    to customize their event
    '''
    state.error = ""
    day_times = []
    durations = []
    inc = .5
    day_range = ((convert_time_to_num(state.end_time) - convert_time_to_num(state.start_time))//50)+1
    start = find_start(state.start_time, HOURS)
    for i in range(start,start+day_range):
        day_times.append(HOURS[i])
    for i in range(start,day_range-1):
        durations.append(inc)
        inc = inc +.5
    return Page(state, [

        Header("New Event"),
        "\n",
        Text(state.error),
        "\n"
        "Event title:",
        TextBox("name"),
        "\n",
        "Day: ",
        SelectBox("day", DAYS),
        "\n Start Time: ",
        SelectBox("start",day_times),
        "\n"
        "Duration:",
        SelectBox("duration", durations),
        Button("Add Event", "add_event"),
        Button("Back","index")
        
        ])

#actually adds an event and catches errors
@route
def add_event(state: State,name:str,day:str,start:str,duration:float)->Page:
    '''
    The updating of the schedule
    to add the event
    '''
    if(name == ""):
        state.error = "error_NO_NAME_GIVEN"
        return event_form(state)
    event = Event(name, day, start, duration)
    state.schedule.append(event)
    state.error = ""
    return index(state)


@route
def remove_form(state:State)->Page:
    '''
    Page that allows the user to
    remove a chosen event
    '''
    if(state.schedule == []):
        state.error = "No events to remove!"
        return index(state)
    #list of scheduled events
    drop_down = []
    for event in state.schedule:
        drop_down.append(event.name)
    return Page(state, [
        "Select the event you want to remove:",
        SelectBox("remove",drop_down),
        Button("Done", "remove_event"),
        Button("Back","index")

        
        ])
@route
def remove_event(state:State,remove:str)->Page:
    '''
    Updates the state to remove the event, this was a special form
    of the for loop that AI showed me
    '''
    state.schedule = [event for event in state.schedule if event.name != remove]
    return index(state)

@route
def customize_form(state:State):
    '''
    Allows the user to choose a custom time range
    and color for schedule
    '''
    return Page(state, [
        Text(state.error),
        Text("WARNING THIS WILL WIPE YOUR CURRENT SCHEDULE"),
        "\n",
        "Pick Start Time",
        SelectBox("start", HOURS),
        "Pick End Time",
        SelectBox("end", HOURS),
        "\nTable Color (enter a value 0-255 for each)",
        "\nRed",
        TextBox("r"),
        "\nGreen",
        TextBox("g"),
        "\nBlue",
        TextBox("b"),
        "\n",
        Button("Confirm Changes","enact_customs"),
        Button("Back","index")
        ])
    
@route
def enact_customs(state:State,start:str,end:str,r:str,g:str,b:str)->Page:
    '''
    Updates the states to the users customizations,
    WIPES THE USER'S PREVIOUS SCHEDULE
    '''
    if(start == end):
        state.error = "error_NO_TIME_RANGE_POSSIBLE"
        return customize_form(state)
    state.start_time = start
    state.end_time = end
    state.r = r
    state.g = g
    state.b = b
    state.error = ""
    return index(state)

def find_start(time:str, times:list)->int:
    '''
    Finds the start of the hours array
    '''
    count = 0
    for t in times:
        if(time != t):
            count = count+1
        else:
            return count
    return 0


#helper functions
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
    
    






        
start_server(State([],"6:00AM","8:00PM",date.today(),0,255,255,255,""))