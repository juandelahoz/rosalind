#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')

N = 
comp = {"A":"T", "T":"A", "C":"G", "G":"C"}

for line in file:
	for nucl in line.strip():
		rev_comp = comp[nucl] + rev_comp

print( rev_comp )
