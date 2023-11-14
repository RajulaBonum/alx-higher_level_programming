#!/usr/bin/python3
len_tuple = __import__('1-len_tuple').len_tuple

sentence = "At school, I learnt C!"
length, first = len_tuple(sentence)
print("Length: {:d} - First character: {}".format(length, first))
