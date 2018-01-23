#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
query = inp.readline().strip()
reference = inp.readline().strip()
mismatch = int(inp.readline().strip())

def HammingDistance( pattern, pattern_ ):
	distance = 0
	for i in range(len(pattern)):
		if pattern[i] != pattern_[i]:
			distance += 1
	return distance

def ApproximatePatternCount( text, pattern, d ):
	count = 0
	position = []
	for i in  range(len(text) - len(pattern)):
		if HammingDistance(pattern, text[i:i+len(pattern)]) <= d:
			count += 1
			position.append(i)
	return (count,position)

print( ApproximatePatternCount( reference, query, mismatch ) )
