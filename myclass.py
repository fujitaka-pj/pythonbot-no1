# -*- coding: utf-8 -*-

class Counter:
  def __init__(self):
    self.word_dictionary = {}
    try:
      file = open('word_dictionary.txt', 'r')
    except:
      return
    # 保存の時に「key value」となるように保存しておく
    for word in file:
      words = word.split()
      self.word_dictionary[words[0]] = int(words[1])

  def add_words(self, sentence):
    words = sentence.split()
    for word in words:
      if word in self.word_dictionary:
        self.word_dictionary[word] = self.word_dictionary[word] + 1
      else:
        self.word_dictionary[word] = 1

  def get_word_dictionary(self):
    print(sorted(self.word_dictionary.items(), key=lambda x: x[0]))

  def write_dictionary(self):
    file = open('word_dictionary.txt', 'w')
    for key in self.word_dictionary:
      dictionary = key
      dictionary += ' '
      dictionary += str(self.word_dictionary[key])
      file.write(dictionary)
      file.write('\n')
    file.close()
