#!/usr/bin/python

import sys
import numpy as np

file = open(sys.argv[1], 'r')
first_line = 1
profile = {"A":0, "C":1, "G":2, "T":3}
profk = ["A","C","G","T"]

for line in file:
	if not line.startswith(">"):
		line = line.strip()
		if first_line == 1:
			row = [0] * len(line)
			for i in profile:
				profile[i] = list(row)
			first_line = 0
		for i in range(len(line)):
			profile[line[i]][i] += 1

consensus = ""
for i in range(len(row)):
	common = max([profile[x][i] for x in profk])
	for x in profk:
		if profile[x][i] >= common:
			ancestral = x
	consensus = consensus + ancestral

print(consensus)
for i in profk:
	print(i, " ".join(map(str, profile[i])))
