#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
reference = inp.readline().strip()
k,L,t = [int(i) for i in inp.readline().strip().split(" ")]

def SymbolToNumber(symbol):
	symbols = {"A":0,"C":1,"G":2,"T":3}
	return symbols[symbol]

def NumberToSymbol(number):
	numbers = {0:"A",1:"C",2:"G",3:"T"}
	return numbers[number]

def PatternToNumber(pattern):
	if pattern == "":
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def NumberToPattern(index, k):
	if k == 1:
		return NumberToSymbol(index)
	prefixIndex = int(index/4)
	r = index%4
	symbol = NumberToSymbol(r)
	PrefixPattern = NumberToPattern(prefixIndex,k-1)
	return PrefixPattern + symbol

def ComputingFrequencies(text, k):
	frequencies = [0] * (4**k)
	for i in range(len(text)-k+1):
		frequencies[PatternToNumber( text[i:i+k] )] += 1
	return frequencies

def ClumpFinding(Genome, k, t, L):
	clumps = {-1}
	frequencies = ComputingFrequencies(Genome[:L],k)
	for i in range(4**k):
		if frequencies[i] >= t:
			clumps.add(NumberToPattern(i,k))
	for i in range(len(Genome)-L):
		kmer_m = PatternToNumber(Genome[i:i+k])
		kmer_p = PatternToNumber(Genome[i+L-k+1:i+L+1])
		if frequencies[kmer_m] > 0:
			frequencies[kmer_m] -= 1
		frequencies[kmer_p] += 1
		if frequencies[kmer_p] >= t:
			clumps.add(NumberToPattern(kmer_p,k))
	clumps.remove(-1)
	clumps = list(clumps)
	clumps.sort()
	return clumps

print( ClumpFinding(reference,k,t,L) )
