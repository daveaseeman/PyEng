#!/usr/bin/python
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

f = open("birds.txt", "r")
data = f.read()
f.close()

print(data)
words = data.split(" ")
lines = data.split("\n")
num_words = len(words)
num_lines = len(lines)
print("The number of words is ", num_words)
print("The number of lines is ", num_lines)
