#!/usr/bin/python
import sys

file  = open(sys.argv[1],"r")
kmers = []
for line in file:
	kmers.append( line.strip() )

for prefix in kmers:
	for sufix in kmers:
		if prefix != sufix:
			if prefix[1:] == sufix[:-1]:
				print(prefix + " -> " + sufix)
