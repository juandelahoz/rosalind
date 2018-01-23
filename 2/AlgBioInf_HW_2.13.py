#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
reference = inp.readline().strip()

def MinimumSkew(reference):
	skew = 0
	min_sk = 0
	mins_sk = []
	for i in range(len(reference)):
		if reference[i] == "C":
			skew -= 1
		elif reference[i] == "G":
			skew += 1
		if skew <= min_sk:
			if skew < min_sk:
				min_sk = skew
				mins_sk = []
			mins_sk.append(i+1)
	return mins_sk

print( MinimumSkew( reference ) )
