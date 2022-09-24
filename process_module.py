#_______________Imports__________________
import string
from time_module import get_date, get_time
from database import *
from internet_module import check_net_con, check_wiki
import nc_module as nc
#from summarize import summ_txt



#_________Process Method__________
def process(query):
    #______Fetching Answer from Database_____
    answer = get_answer(query)
    #______Voice Command________
    if answer == "loop":    #if voice not clear
        return 0
    elif answer == "vc_on":
        c_vc = get_asd("voice_command")
        if c_vc == "on":
            return "Voice command is already on"
        else:
            put_asd("voice_command", "on")
            return "Voice command is activated"
    elif answer == "vc_off":
        c_vc = get_asd("voice_command")
        if c_vc == "off":
            return "Voice command is already off"
        else:
            put_asd("voice_command", "off")
            return "Voice command is deactivated"



    #____________Natural Conversation_______________
    elif answer == "greet":
        return nc.greet()

    elif answer == "identity":
        return nc.identity()
    
    elif answer == "task_can_do":
        return nc.task_can_do()
    
    elif answer == "manners":
        return nc.manners()

    elif answer == "bye":       
        x = nc.bye()
        return x  


    
    #_________Checking Time__________
    elif answer == "get time details":
        return("Time is "+ str(get_time()) + "")

    
    #___________Tell Today's Date_________
    elif answer == "tell date":
        return "Today's date is " + str(get_date()) + ""



    #______Checking Internet Connection_______
    elif answer == "check internet connection":
        if check_net_con():
            return "Internet is connected"
        else:
            return "Internet is not connected"

    
#_______________Wikipedia__________________
    elif "who is" in query or "what is" in query or "tell me about" in query and answer == "":
        w = check_wiki(query)
        return w

    #_______________If the input is not in Database________________
    
    else:
        return "Sorry, I don't understand"
            
