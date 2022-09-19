#__________Imports___________
import urllib.request
import wikipediaapi


#_______CHecking Internet Connection________
def check_net_con():
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False

#   import socket
#   IP=socket.gethostbyname(socket.gethostname())
#   if IP=="127.0.0.1":
#     return False
#   else:
#     return True


#________Checking Wikipedia________
def check_wiki(query):
    query = query.lower()
    query = query.replace("who is","")
    query = query.replace("who's","")
    query = query.replace("what is","")
    query = query.replace("what's","")
    query = query.replace("do you know","")
    query = query.replace("tell me about","")
    query = query.strip()
    query = query.title()
    try:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        data = wiki_wiki.page(query).summary
        sum = data.split("\n")
        return sum[0]
        #return data
    except Exception as e:
        return ""
