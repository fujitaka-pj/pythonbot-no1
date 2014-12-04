# -*- coding: utf-8 -*-
import sys
import random
import datetime

class Counter:
  def __init__(self):
    self.word_dictionary = {}

  def add_words(self, sentence):
    words = sentence.split()
    for word in words:
      if word in self.word_dictionary:
        self.word_dictionary[word] = self.word_dictionary[word] + 1
      else:
        self.word_dictionary[word] = 1

  def get_word_dictionary(self):
    print(sorted(self.word_dictionary.items(), key=lambda x: x[0]))

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
  save_file(conversations)
