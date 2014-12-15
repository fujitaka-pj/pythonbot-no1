# -*- coding: utf-8 -*-
import sys
import random
import datetime

from myclass import Counter

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
  return todaydetail.strftime('%Y%m%d%H%M%S') + '.log'

def save_file(conversations):
  file = open(filename(), 'w')
  for conversation in conversations:
    file.write(conversation)
    file.write('\n')
  file.close()

if __name__ == '__main__':

  print('Hey, Welcome!!')
  conversations = []
  counter = Counter()
  for value in range(3):
    user_input = input()
    conversations.append(user_input)
    counter.add_words(user_input)

    if user_input == 'exit':
      print('Bye')
      conversations.append('Bye')
      break

    bot_reply = reply(user_input)
    print(bot_reply)
    conversations.append(bot_reply)

  counter.get_word_dictionary()
  counter.draw_chart()
  counter.write_dictionary()
  save_file(conversations)
