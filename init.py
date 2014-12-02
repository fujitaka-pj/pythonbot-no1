# -*- coding: utf-8 -*-
import sys
import random
import datetime

def reply(user_input=''):
  selection = int(random.random() * 3)
  if selection == 0:
    return 'How are you?'
  elif selection == 1:
    return 'I am fine.'
  else:
    return user_input

def filename():
  todaydetail = datetime.datetime.today()
  return todaydetail.strftime('%Y%m%d%H%M%S') + '.txt'

def save_file(conversations):
  file = open(filename(), 'w')
  for conversation in conversations:
    file.write(conversation)
    file.write('\n')
  file.close()

if __name__ == '__main__':
  print('Hey, Welcome!!')
  conversations = []
  for value in range(3):
    user_input = input()
    conversations.append(user_input)

    if user_input == 'exit':
      print('Bye')
      conversations.append('Bye')
      break

    bot_reply = reply(user_input)
    print(bot_reply)
    conversations.append(bot_reply)

  save_file(conversations)
