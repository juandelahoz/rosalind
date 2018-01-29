#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
seq = inp.readline().strip().split(" ")
length = int(inp.readline().strip())

words = []
# add each letter
for i in range(length-1):
	if i == 0:
		words2 = list(seq)
	else:
		words2 = list(words)
	for w2 in words2:
		for w in seq:
			w3 = w2+w
			words.append(w3)

words = [x for x in words if len(x) == length]

words.sort()
print(words)

### print output ###
out = open("answer.txt",'w')
for i in words:
	out.write(i + "\n")
out.close()
