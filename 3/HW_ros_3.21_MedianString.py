#!/usr/bin/python
import sys

file = open(sys.argv[1],"r")
k = int(file.readline().strip())
scores = [0] * (4**k)
NumberToSymbol = { 0:"A", 1:"C", 2:"G", 3:"T" }

def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol[index]
	prefixIndex = int(index/4)
	r = index%4
	symbol = NumberToSymbol[r]
	PrefixPattern = NumberToPattern(prefixIndex,k-1)
	return PrefixPattern + symbol

for line in file:
	dna_i = line.strip()
	for p in range(len(scores)):
		patt = NumberToPattern(p,k)
		d_patt_text = k
		for i in range(len(dna_i)-k+1):
			H_distance = sum([1 if patt[j] != dna_i[i:i+k][j] else 0 for j in range(k)])
			if d_patt_text > H_distance :
				d_patt_text	= H_distance
		scores[p] += d_patt_text

d_min = sum(scores)
j = -1
for i in range(len(scores)):
	if scores[i] <= d_min:
		d_min = scores[i]
		j = i 

print(NumberToPattern(j,k))