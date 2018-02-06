#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")

m = 0
for line in inp:
	a,b = map(int,line.strip().split())
	if m == 0:
		d = [0] * a
	else:
		d[a-1] += 1
		d[b-1] += 1
	m += 1

print(" ".join(map(str,d)))
