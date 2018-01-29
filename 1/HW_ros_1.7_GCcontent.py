#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')

seqs = {}
nt_val = {"A":0.0, "T":0.0, "C":1.0, "G":1.0}
highest = ("",0.0)
nt_tot = 0

for line in file:
	if line.startswith(">"):
		if nt_tot > 0:
			seqs[name] = (gc_cnt / nt_tot) * 100
			if highest[1] < seqs[name]:
				highest = (name,seqs[name])
		name = line.strip()[1:]
		nt_tot = 0.0
		gc_cnt = 0.0
	else:
		for nucl in line.strip():
			gc_cnt += nt_val[nucl]
			nt_tot += 1.0

seqs[name] = (gc_cnt / nt_tot) * 100
if highest[1] < seqs[name]:
	highest = (name,seqs[name])


print( highest[0] )
print( highest[1] )
print( seqs )