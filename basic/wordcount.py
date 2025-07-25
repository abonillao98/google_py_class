#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def get_dict_of_words(filename):
  words_list = []
  f = open(filename,'r')

  for line in f:
    line_lower = line.lower()
    line_lower_list = line_lower.split()
    words_list = words_list + line_lower_list

  f.close()

  dict_words = {}

  for word in words_list:
    if word not in dict_words:
      dict_words[word] = 1
    else:
      dict_words[word] += 1

  return dict_words
  
def print_words(filename):
  dict_words = get_dict_of_words(filename)
  print("word -> count")
  keys = dict_words.keys()
  
  for key in sorted(keys):
    print(key," -> ", dict_words[key])
  

def print_top(filename):
  dict_words = get_dict_of_words(filename)
  print("Top 20 most common words\nword -> count")

  items = dict_words.items()
  items = sorted(items, key=lambda items: items[1], reverse=1)

  i = 0
  for item in items:
    print(item[0], '->', item[1])
    i +=1

    if i>=20: break



###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
