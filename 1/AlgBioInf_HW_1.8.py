#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')

d_h = 0
ali = ""

seq1 = file.readline().strip()
seq2 = file.readline().strip()

if len(seq1) != len(seq2):
	exit("Sorry, both sequences MUST be the same length")

for i in range(len(seq1)):
	if seq1[i] != seq2[i]:
		d_h += 1
		ali += "|"
	else:
		ali += " "

print(seq1)
print(ali + " -> " + str(d_h))
print(seq2)