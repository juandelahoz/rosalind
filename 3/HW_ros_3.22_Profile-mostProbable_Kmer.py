#!/usr/bin/python
import sys

file  = open(sys.argv[1],"r")
dna   = file.readline().strip()
k = int(file.readline().strip())
probs = [1] * (len(dna)-k+1)
profile = {}
profile["A"] = map(float, file.readline().split(" ") )
profile["C"] = map(float, file.readline().split(" ") )
profile["G"] = map(float, file.readline().split(" ") )
profile["T"] = map(float, file.readline().split(" ") )

max_p = 0
for i in range(len(probs)):
	kmer = dna[i:i+k]
	for n in range(k):
		nt = kmer[n]
		probs[i] *= profile[nt][n]
	if max_p < probs[i]:
		max_p = probs[i]
		motif = kmer

print(motif,max_p)

