#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')
result = open("answer.txt",'w')
count = 1
for line in file:
	if( count%2 == 0):
		result.write(line)
	count += 1
result.close()
