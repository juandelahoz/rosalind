#!/usr/bin/python

import sys
import numpy as np

file = open(sys.argv[1], 'r')
#rowm = {"A":0, "C":1, "G":2, "T":3}
#profilem = [0] * 4
first_line = 1
profile = {"A":0, "C":1, "G":2, "T":3}

for line in file:
	if not line.startswith(">"):
		if first_line == 1:
			row = [0] * len(line)
			for i in profile:
#				profilem[i] = list(row)
				profile[i] = list(row)
			first_line = 0
#			profilem = np.matrix(profilem)
		for nucl in line.strip():
#			gc_cnt += nt_val[nucl]
#			nt_tot += 1.0

print(profile)