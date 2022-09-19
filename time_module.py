from datetime import datetime, date


#____________Getting Date_______________
def get_date():
    return date.today()

#______________Telling Time_____________
def get_time():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    return current_time

#_____________Getting Hour________________

def get_hour():
    now = datetime.now()
    current_hour = now.strftime("%H")
    return current_hour