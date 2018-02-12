#!/Users/juan/anaconda/bin/python

# read FASTA format
import sys

inp = open(sys.argv[1],"r")

seq = ""
for line in inp:
	if line.startswith(">"):
		seq = ""
	else:
		seq += line.strip()

print(seq)

fa = [0]

for j in range(1,len(seq)):
	for k in range(


print(fa)