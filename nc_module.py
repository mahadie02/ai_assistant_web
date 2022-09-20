#__________Imports___________
import random as r

def greet():
    greet1 = ['Hi', 'Hii', 'Hello', 'Yes']
    greet2 = [' Sir',' Boss', '']
    greet = r.choice(greet1) + r.choice(greet2)
    return greet



def identity():
    id1 = ['Well,', 'As you see,', 'It seems', "Perhaps", "Isn't is obvius that"]
    id2 = [" a Personal Assistant based on Artificial Intelligence", " an Artificial Intelligence based Personal Assistant"]
    id3 = [" and I can help you perfrom different tasks with ease", " and I can talk to you if you want", " and I can do certain things based on your commands"]
    id = r.choice(id1) + " I am" + r.choice(id2) + r.choice(id3)
    return id

def task_can_do():
    task1 = ["I can", "I do", "I will"]
    task2 = [" help with the details of our shop", " help with making purchase decisions", " answer any of your queries"]
    task = r.choice(task1) + r.choice(task2)
    return task

def manners():
    man1 = ["I think", "I guess", "As you see", "As I'm a software"]
    man2 = [" I am good.", "I'm pretty good", " I'm always good.", " I'm ok if I have no bug.", " I'm happy if you are happy with me."]
    man3 = [" How are you", " How about you", " How are you doing", " How is your day", " How is it going", " How's life", " Is everything ok"]
    man4 = [" sir?", " boss?", "?"]
    man = r.choice(man1) + r.choice(man2) + r.choice(man3) + r.choice(man4)
    return man


def bye():
    bye1 = ["Ok bye", "See you again", "Take care, bye", "See you later"]
    bye2 = [" sir", " boss", ""]
    bye = r.choice(bye1) + r.choice(bye2)
    return bye
