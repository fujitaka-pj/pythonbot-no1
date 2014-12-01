# -*- coding: utf-8 -*-
import sys
import random

def reply():
  selection = int(random.random() * 3)
  if selection == 0:
    print("How are you??")
  elif selection == 1:
    print("I am fine.")
  else:
    print(selection)

for value in range(3):
  user_input = sys.stdin.readline()
  print(user_input)
  reply()
  if user_input == 'exit\n':
    print("Bye")
    break
