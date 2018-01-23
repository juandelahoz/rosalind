#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')
result = open("answer.txt",'w')

words = {}

for line in file:
	for word in line.split():
		if word not in words:
			words[word] = 1
		else:
			words[word] +=1
for a, b in words.items():
	result.write(str(a) + " " + str(b) + "\n")

result.close()
