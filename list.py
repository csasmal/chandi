#get your input sentence

import sys
import string
my_sentence = "Jenny, harry, doggy and theri mamas"
my_sentence = my_sentence.lower()

characters = set(my_sentence)
alphabet = string.lowercase
letters = characters.intersection(alphabet)

print len(letters)
