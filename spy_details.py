# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:31:42 2018

@author: HelloWorld
"""
from datetime import datetime
class Spy:
  def __init__(self, name, salutation, age, rating):
    self.spy_name = name
    self.spy_salutation = salutation
    self.spy_age = age
    self.spy_rating = rating
    self.spy_online = True
    self.chats = []
    self.status = ["Jai Hind"]

spy = Spy('Chaudhary', 'Mr.', 21, 5)
friend_one = Spy('Vipanshu', 'Mr.', 21, 4.9)
friend_two = Spy('Matta', 'Ms.', 21, 4.39)
friend_three = Spy('Atala', 'Jr', 19, 4.95)

friends = [friend_one, friend_two, friend_three]

class ChatMessage:
  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me