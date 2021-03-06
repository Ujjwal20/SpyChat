# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:32:52 2018

@author: HelloWorld
"""
#importing packages from anther file
#isstring to check whether the name is string
from spy_details import spy_name,spy_salutation,spy_rating,spy_age,spy_online,status
from isstring import isstring

#First message
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? \n  "
existing = raw_input(question)
def add_status(current_status_message):

    updated_status_message = None

    
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

   
    default = raw_input("Do you want to select from the older status (Y/N)? ")

    if default == "N":
        new_status_message = raw_input("What status message do you want to set? ")

        
        if len(new_status_message) > 0:
            status.append(new_status_message)
            updated_status_message = new_status_message

    elif default == 'Y':
        item_position = 1

        for message in status:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = input("\nChoose from the above messages ")

       
        if len(status) >= message_selection:
            updated_status_message = status[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'

    return updated_status_message



def start_chat(spy_name,spy_age, spy_rating):
   spy_name = spy_salutation + " " + spy_name
   show_menu =True
   current_status_message =status
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
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)
            if menu_choice == 1:
                current_status_message = add_status(current_status_message)          
            else:
                show_menu = False
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