#!/Users/juan/anaconda/bin/python

# read FASTA format
import sys

inp = open(sys.argv[1],"r")

taxa = []
tids = []
seq = ""
fline = False
for line in inp:
	if line.startswith(">"):
		tids.append(line.strip()[1:])
		if fline:
			taxa.append(seq)
			seq = ""
		fline = True
	else:
		seq += line.strip()
taxa.append(seq)
n = len(taxa)

# create distance matrix
D = [0] * n

for i in range(n):
	s2 = []
	for j in range(n):
		l = len(taxa[i])
		s2.append( sum([1.0 if taxa[i][k] != taxa[j][k] else 0.0 for k in range(l)]) /l )
		D[i] = s2

# print matrix
for i in range(n):
	print(" ".join(map(str,D[i])))
