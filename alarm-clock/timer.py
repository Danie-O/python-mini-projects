# Alarm sound can be downloaded from: https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203

# import dependencies
from playsound import playsound
import time
from datetime import date, datetime as dt

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def find_timedelta(alarm_time: str) -> int:
    """Calculate difference(timedelta) between current time & when user wants alarm to sound, in seconds."""
    current_time = dt.now()
    todays_date = date.today().strftime("%Y-%m-%d")
    alarm_time = " ".join([todays_date, alarm_time])

    deadline = dt.strptime(alarm_time, "%Y-%m-%d %H:%M:%S")
    delta = deadline - current_time
    seconds = int(delta.total_seconds())
    return seconds

# find_timedelta("19:30:00")

def set_alarm(by_seconds: bool=False, by_time: bool=False):
    """Display countdown in seconds and sound alarm when countdown elapses."""
    time_elapsed = 0
    print(CLEAR)

    if by_seconds:
        seconds = int(input("How many seconds from now do you want to set alarm: ")) 
    elif by_time:
        deadline_by_time = input("What time do you want to set an alarm for today: (HH:MM:SS) eg. 19:23:00 == 7:30pm    ")
        seconds = find_timedelta(deadline_by_time)

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN} Alarm would sound in: {minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")


set_alarm(by_time=True)
# set_alarm(by_seconds=True)
