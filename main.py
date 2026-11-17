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
    '12:00AM', '12:05AM', '12:10AM', '12:15AM', '12:20AM', '12:25AM',
    '12:30AM', '12:35AM', '12:40AM', '12:45AM', '12:50AM', '12:55AM',
    '1:00AM', '1:05AM', '1:10AM', '1:15AM', '1:20AM', '1:25AM',
    '1:30AM', '1:35AM', '1:40AM', '1:45AM', '1:50AM', '1:55AM',
    '2:00AM', '2:05AM', '2:10AM', '2:15AM', '2:20AM', '2:25AM',
    '2:30AM', '2:35AM', '2:40AM', '2:45AM', '2:50AM', '2:55AM',
    '3:00AM', '3:05AM', '3:10AM', '3:15AM', '3:20AM', '3:25AM',
    '3:30AM', '3:35AM', '3:40AM', '3:45AM', '3:50AM', '3:55AM',
    '4:00AM', '4:05AM', '4:10AM', '4:15AM', '4:20AM', '4:25AM',
    '4:30AM', '4:35AM', '4:40AM', '4:45AM', '4:50AM', '4:55AM',
    '5:00AM', '5:05AM', '5:10AM', '5:15AM', '5:20AM', '5:25AM',
    '5:30AM', '5:35AM', '5:40AM', '5:45AM', '5:50AM', '5:55AM',
    '6:00AM', '6:05AM', '6:10AM', '6:15AM', '6:20AM', '6:25AM',
    '6:30AM', '6:35AM', '6:40AM', '6:45AM', '6:50AM', '6:55AM',
    '7:00AM', '7:05AM', '7:10AM', '7:15AM', '7:20AM', '7:25AM',
    '7:30AM', '7:35AM', '7:40AM', '7:45AM', '7:50AM', '7:55AM',
    '8:00AM', '8:05AM', '8:10AM', '8:15AM', '8:20AM', '8:25AM',
    '8:30AM', '8:35AM', '8:40AM', '8:45AM', '8:50AM', '8:55AM',
    '9:00AM', '9:05AM', '9:10AM', '9:15AM', '9:20AM', '9:25AM',
    '9:30AM', '9:35AM', '9:40AM', '9:45AM', '9:50AM', '9:55AM',
    '10:00AM', '10:05AM', '10:10AM', '10:15AM', '10:20AM', '10:25AM',
    '10:30AM', '10:35AM', '10:40AM', '10:45AM', '10:50AM', '10:55AM',
    '11:00AM', '11:05AM', '11:10AM', '11:15AM', '11:20AM', '11:25AM',
    '11:30AM', '11:35AM', '11:40AM', '11:45AM', '11:50AM', '11:55AM',
    '12:00PM', '12:05PM', '12:10PM', '12:15PM', '12:20PM', '12:25PM',
    '12:30PM', '12:35PM', '12:40PM', '12:45PM', '12:50PM', '12:55PM',
    '1:00PM', '1:05PM', '1:10PM', '1:15PM', '1:20PM', '1:25PM',
    '1:30PM', '1:35PM', '1:40PM', '1:45PM', '1:50PM', '1:55PM',
    '2:00PM', '2:05PM', '2:10PM', '2:15PM', '2:20PM', '2:25PM',
    '2:30PM', '2:35PM', '2:40PM', '2:45PM', '2:50PM', '2:55PM',
    '3:00PM', '3:05PM', '3:10PM', '3:15PM', '3:20PM', '3:25PM',
    '3:30PM', '3:35PM', '3:40PM', '3:45PM', '3:50PM', '3:55PM',
    '4:00PM', '4:05PM', '4:10PM', '4:15PM', '4:20PM', '4:25PM',
    '4:30PM', '4:35PM', '4:40PM', '4:45PM', '4:50PM', '4:55PM',
    '5:00PM', '5:05PM', '5:10PM', '5:15PM', '5:20PM', '5:25PM',
    '5:30PM', '5:35PM', '5:40PM', '5:45PM', '5:50PM', '5:55PM',
    '6:00PM', '6:05PM', '6:10PM', '6:15PM', '6:20PM', '6:25PM',
    '6:30PM', '6:35PM', '6:40PM', '6:45PM', '6:50PM', '6:55PM',
    '7:00PM', '7:05PM', '7:10PM', '7:15PM', '7:20PM', '7:25PM',
    '7:30PM', '7:35PM', '7:40PM', '7:45PM', '7:50PM', '7:55PM',
    '8:00PM', '8:05PM', '8:10PM', '8:15PM', '8:20PM', '8:25PM',
    '8:30PM', '8:35PM', '8:40PM', '8:45PM', '8:50PM', '8:55PM',
    '9:00PM', '9:05PM', '9:10PM', '9:15PM', '9:20PM', '9:25PM',
    '9:30PM', '9:35PM', '9:40PM', '9:45PM', '9:50PM', '9:55PM',
    '10:00PM', '10:05PM', '10:10PM', '10:15PM', '10:20PM', '10:25PM',
    '10:30PM', '10:35PM', '10:40PM', '10:45PM', '10:50PM', '10:55PM',
    '11:00PM', '11:05PM', '11:10PM', '11:15PM', '11:20PM', '11:25PM',
    '11:30PM', '11:35PM', '11:40PM', '11:45PM', '11:50PM', '11:55PM',
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