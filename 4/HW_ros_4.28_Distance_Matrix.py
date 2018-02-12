#!/Users/juan/anaconda/bin/python

# read FASTA format
import sys

inp = open(sys.argv[1],"r")

seqfa = []
seqid = []
seq = ""
fline = False
for line in inp:
	if line.startswith(">"):
		seqid.append(line.strip()[1:])
		if fline:
			seqfa.append(seq)
			seq = ""
		fline = True
	else:
		seq += line.strip()
seqfa.append(seq)
n = len(seqfa)

# create distance matrix
D = [0] * n

for i in range(n):
	s2 = []
	for j in range(n):
		l = len(seqfa[i])
		s2.append( sum([1.0 if seqfa[i][k] != seqfa[j][k] else 0.0 for k in range(l)]) /l )
		D[i] = s2

# print matrix
for i in range(n):
	print(" ".join(map(str,D[i])))
