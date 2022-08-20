from numpy import random as rnd
import json

path = 'dcts/'
name = 'Tvortsyi_zaklinaniy.txt'
to_whitespace = '.-'
stop_words = ['И.', 'Г.', 'Ф.', 'notes', 'Прэтчетт', 'Терри', 'Нилу', 'Гэйману']
whitespace = '\t\n\r\x0b\x0c'
marks = '"#$%&\'()*+/:;<=>@[\\]^_`{|}~.,1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*—“”…!?.'

def get_text(path = path, name = name, whitespace = whitespace, marks = marks, stop_words = stop_words):
  '''
  function cleans the text
  input -
     path wheh located text in .txt format,
     name of the txt file
     to_whitespace - what we change to whitespace
     rep_dct - words to replace
     whitespace - symbols to replace
     marks - symbols to replace
  output - list of clear text

  '''
  with open(path + name, encoding="utf-8") as f:
    k = f.read()
    for s in stop_words:
      k = k.replace(s, '')
    for s in to_whitespace:
      k = k.replace(s, ' ')
    for s in marks:
      k = k.replace(s, '')
    for s in whitespace:
      k = k.replace(s, ' ')
    k = k.lower().split()
  return k

def get_pairs(lst):
  '''
  function give pairs word: list of next words or list of previews words
  input: list from get_text()
  output: foreward dictionary with next words and backward dictionary with previews words
  '''
  d = dict()
  dd = dict()
  for i in lst:
    d[i] = []
    dd[i] = []
  for word in d.keys():
    for i in range(len(lst)-1):
      if word == lst[i]:
        d[word] += [lst[i+1]]
  print('forward dict is ready')
  for word in dd.keys():
    for i in range(1,(len(lst))):
      if word == lst[i]:
        dd[word] += [lst[i-1]]
  print('backward dict is ready')
  return d, dd


def sentence(word, dctn1, dctn2, state = 1, ln = 100):
  '''
  function create list of words based by Markov chains.
  input:
      dctn1, dctn2 - forward and backward dictionaries from get_pairs_bin()
      word - word to start of chain
      state: 1 - create sentence by forward dict, 2 - create sentence by backward dict
             3 - create sentence by both dict
      ln - lenght of sentence
  output: list with words based by randomity Markov chains
  '''
  txt = []

  if word not in dctn1.keys() or word not in dctn2.keys():
    word = 'о'
    # print(word)
  if state == 1:
    while len(txt) <= ln:
      nxt = rnd.choice(dctn1.get(word, 'о'))
      # print(word)
      txt.append(nxt)
      word = nxt
      # print(word)
  elif state == 2:
    while len(txt) <= ln:
      nxt = rnd.choice(dctn2.get(word, 'о'))
      txt.append(nxt)
      word = nxt
  elif state == 3:
    while len(txt) <= ln:
      nxt2 = rnd.choice(dctn2.get(word, '.'))
      txt.append(nxt2)
      nxt1 = rnd.choice(dctn1.get(word, '.'))
      txt.append(nxt1)
      word = nxt1
  else:
    while len(txt) <= ln:
      nxt = rnd.choice(dctn1.get(word, '.'))
      txt.append(nxt)
      word = nxt
  return txt

def prnt(lst):
  '''
  function transform list from sentence() to str and print it
  input: list from sentence()
  output: print the sentence
  '''
  s = ''
  for w in lst:
    s += w + ' '
  return s


def load_dct(path = path, tp = 1):
  '''
  load dictionary
  input: path to dictionaries
         tp - type of dictionary: 1 is foreward dict, 2 is backward
  output: loaded dictionary
  '''
  if tp == 1:
    name = 'forward'
  elif tp == 2:
    name = 'backward'
  else:
    name = 'forward'
  with open(f'{path}dct_{name}.json') as f:
    dct = json.load(f)
  return dct


def save_dct(dct, path = path, tp = 1):
  '''
  save dictionaries from get_pairs_bin()
  input: dct - dictionary to save
         path - path to save
         tp - type of dictionary: 1 - forward dictionary, 2 - backward dictionary
  result: saved dictionary
  '''
  if tp == 1:
    name = 'forward'
  elif tp == 2:
    name = 'backward'
  # else:
  #   name = 'both'
  with open(f'{path}dct_{name}.json', 'w') as f:
    json.dump(dct, f)
  print('dict saved')

