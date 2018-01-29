#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
reference = inp.readline().strip()
query = inp.readline().strip()

def PatternCount( text, pattern ):
	count = 0
	position = []
	for i in  range(len(text) - len(pattern) +1):
		if pattern == text[i:i+len(pattern)]:
			count += 1
			position.append(i+1)
	return (count,position)

print( PatternCount( reference, query ) )
