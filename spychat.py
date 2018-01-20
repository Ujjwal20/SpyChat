# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:32:52 2018

@author: HelloWorld
"""
#importing packages from anther file
#isstring to check whether the name is string
from spy_details import spy,Spy,ChatMessage,friends
from isstring import isstring
from steganography.steganography import Steganography
import csv




def add_status(current_status_message):
    updated_status_message = None
#Check for current status
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

  #selecting old status 
    default = raw_input("Do you want to select from the older status (Y/N)? ")
#new status input
    if default == "N":
        new_status_message = raw_input("What status message do you want to set? ")

      #status validity check  
        if len(new_status_message) > 0:
            spy.status.append(new_status_message)
            updated_status_message = new_status_message
#choose from old status
    elif default == 'Y':
        item_position = 1

        for message in spy.status:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = input("\nChoose from the above messages ")

       
        if len(spy.status) >= message_selection:
            updated_status_message = spy.status[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You did not update your status message'

    return updated_status_message


def add_friend():

    
    #Adding new friend
    naam = raw_input("Please add your friend's name: ")
    salutation = raw_input("Are they Mr. or Ms.?: ")

    #new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    age = input("Age?")

    rating = input("Spy rating?")
   
    if len(naam) > 0 and age > 12 and isstring(naam) :
        frd = Spy(naam,salutation,age,rating)
        friends.append(frd)
        print 'Friend Added!'
        with open('friends.csv', 'a') as friends_data:
          writer = csv.writer(friends_data)
          writer.writerow([frd.spy_name,frd.spy_salutation,frd.spy_age,frd.spy_rating])
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    
    
  
    return len(friends)

def select_a_friend():
    item_number = 0
    #Listing out friends
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.spy_name,
                                                   friend.spy_age,
                                                   friend.spy_rating)
        item_number = item_number + 1

    friend_choice = input("Choose from your friends")

    friend_choice_position = friend_choice - 1

    return friend_choice_position

def send_message():
#Choosing friend
    friend_choice = select_a_friend()
#secret message in an image
    original_image = raw_input("What is the name of the image?(Specify the path)")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)
    with open('chat.csv', 'a') as chat_data:
          writer = csv.writer(chat_data)
          writer.writerow([new_chat.message])

    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"

def read_message():
#Selecting a sender
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
#decoding
    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)
    with open('chat.csv', 'a') as chat_data:
          writer = csv.writer(chat_data)
          writer.writerow([new_chat.message])

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"


def start_chat(spy_name,spy_age, spy_rating):
   spy_name = spy_salutation + " " + spy_name
   show_menu =True
   current_status_message =spy.status
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
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)  
            elif menu_choice == 3:
                send_message()
            elif menu_choice ==4:
                read_message()
            else:
                show_menu = False
   else:
        print 'Abhi tumhari umr na hai babua'

#First message
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy.spy_salutation + " " + spy.spy_name + " (Y/N)? \n  "
existing = raw_input(question)
if existing == "Y":
    start_chat(spy.spy_name,spy.spy_age, spy.spy_rating) #working on default value
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