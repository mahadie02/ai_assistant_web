from database import *
from process_module import process

def get_resp(msg):
    reply = process(msg)
    return reply
