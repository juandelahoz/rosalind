#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
seq = inp.readline().strip().split(" ")
length = int(inp.readline().strip())

words = list(seq)
# add each letter
for i in range(1,length):
	words2 = list(words)
	words = []
	for w2 in words2:
		for l in seq:
			word = w2+l
			words.append(word)

words.sort()
print(words)

### print output ###
out = open("answer.txt",'w')
for i in words:
	out.write(i + "\n")
out.close()
