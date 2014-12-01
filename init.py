# -*- coding: utf-8 -*-
import sys
import random

def reply(user_input=""):
  selection = int(random.random() * 3)
  if selection == 0:
    print("How are you??")
  elif selection == 1:
    print("I am fine.")
  else:
    if user_input != "":
      print(user_input)
    else:
      print(selection)

if __name__ == "__main__"
  for value in range(3):
    user_input = sys.stdin.readline()
    print(user_input)
    reply(user_input)
    if user_input == 'exit\n':
      print("Bye")
      break
