#!/usr/bin/python

import sys
import numpy as np

inp = open(sys.argv[1], 'r')
seq = inp.readline().strip()
GCs = [float(i) for i in inp.readline().strip().split(" ")]
Prs = []

for GC in GCs:
	p = 0
	for nt in seq:
		if   nt == "A" or nt == "T":
			p += np.log10((1-GC)/2)
		elif nt == "C" or nt == "G":
			p += np.log10(   GC /2)
	Prs.append(p)

print(Prs)
