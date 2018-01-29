#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')

A=C=G=T=other = 0

for line in file:
	for letter in line:
		if letter == "A":
			A += 1
		elif letter == "C":
			C += 1
		elif letter == "G":
			G += 1
		elif letter == "T":
			T += 1
		else:
			other += 1

print( str(A) + " " + str(C) + " " + str(G) + " " + str(T))
