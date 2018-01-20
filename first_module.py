# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:32:52 2018

@author: HelloWorld
"""
#importing packages from anther file
#isstring to check whether the name is string
from spy_details import spy_name,spy_salutation,spy_rating,spy_age,spy_online
from isstring import isstring
#First message
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? \n  "
existing = raw_input(question)
def start_chat(spy_name,spy_age, spy_rating):
   spy_name = spy_salutation + " " + spy_name
 #Age Check   
   if spy_age > 12 and spy_age < 50:
        print "Your rating is:" + str(spy_rating)
        #Comment on spy rating
        if spy_rating > 4.5:
            print 'Ek Number!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'Kya bt Kya bt Kya bt.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'Tumse na ho payega'
        print "Spy Authenticated. Welcome " + spy_name + " age: " + str(spy_age) + " with rating of: " + str(spy_rating) + " glad to have you onboard" 
   else:
        print 'Abhi tumhari umr na hai babua'

if existing == "Y":
    start_chat(spy_name,spy_age, spy_rating) #working on default value
else:
    spy_name = ''   #making values null for new value
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_online = False


    spy_name = raw_input("Welcome to spy chat, what's your name: ")
    #checking for a valid name
    if len(spy_name) > 0 and isstring(spy_name):
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy_age = input("What is your age?")
        spy_rating = input("What is your spy rating?")
        spy_online = True
        start_chat(spy_name, spy_age, spy_rating)
    else:
        print 'Please add a valid spy name'