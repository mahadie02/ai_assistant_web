#_______________Imports_______________
import sqlite3

#________Creating Database Connection________
def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection


#________Fetching Data from Database________
def get_qna():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM QuestionsAndAnswers")
    return cur.fetchall()


#________Storing New Data into Database________
def put_qna(question, answer):
    con = create_connection()
    cur = con.cursor()
    query = "INSERT INTO QuestionsAndAnswers VALUES('" + question + "','" + answer + "')"
    cur.execute(query)
    con.commit()



#________Retrieving Answer for any Given Question________
def get_answer(question):
    rows = get_qna()
    answer = ""
    for row in rows:
       if row[0].lower() in question.lower():
         answer = row[1]
         break
    return answer


#_________Fetching Assistant Name________
def get_name():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM assistant_details WHERE name = 'assistant_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


#__________Fetching if Speech is On or OFF_________
def get_speech_status():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM assistant_details WHERE name = 'speech'"
    cur.execute(query)
    return cur.fetchall()[0][0]


#_____________Get Assistant details____________
def get_asd(name):
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM assistant_details WHERE name = '"+name+"'"
    cur.execute(query)
    return cur.fetchall()[0][0] 



#______________Update Assistant Details_____________
def put_asd(name,value):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE assistant_details SET value = '"+value+"' WHERE name = '"+name+"'"
    cur.execute(query)
    con.commit()

    

#_________Updating Assistant Name________
def update_name(new_name):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE assistant_details SET value = '" + new_name + "' WHERE name = 'assistant_name'"
    cur.execute(query)
    con.commit()


#_____________Set Last Seen Date_____________
def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE assistant_details SET value = '" + str(last_seen_date) + "' WHERE name = 'last_seen_date'"
    cur.execute(query)
    con.commit()


#_______________Get Last Seen Date_____________
def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM assistant_details WHERE name = 'last_seen_date'"
    cur.execute(query)
    return cur.fetchall()[0][0]


#_______________Speech On/Off__________________
def set_speech_off():
    con = create_connection()
    cur = con.cursor()
    query = "UPDATE assistant_details SET value = 'off' WHERE name = 'speech'"
    cur.execute(query)
    con.commit()
    return "Speech turned off"


def speech_on_off():
    con = create_connection()
    cur = con.cursor()
    query = "SELECT value FROM assistant_details WHERE name = 'speech'"
    cur.execute(query)
    switch = cur.fetchall()[0][0]

    if switch == "on":
        return True
    else:
        return False





