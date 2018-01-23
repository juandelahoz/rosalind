#!/usr/bin/python

import sys

inp = open(sys.argv[1], 'r')
reference = inp.readline().strip()
k,L,t = [int(i) for i in inp.readline().strip().split(" ")]

def SymbolToNumber(symbol):
	if symbol == "A":
		return 0
	elif symbol == "C":
		return 1
	elif symbol == "G":
		return 2
	elif symbol == "T":
		return 3

def NumberToSymbol(number):
	if number == 0:
		return "A"
	elif number == 1:
		return "C"
	elif number == 2:
		return "G"
	elif number == 3:
		return "T"

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

def FrequentWords(text,k):
	frequencies = ComputingFrequencies(text,k)
	most_freq = max(frequencies)
	frequent = []
	for i in range((4**k)):
		if(frequencies[i] == most_freq):
			frequent.append(i)
	return frequent

def ClumpFinding(Genome, k, t, L):
	FrequentPatterns = []
	Clumps = [False] * (4**k)
	for i in range(len(Genome)-L+1):
		text = Genome[i:i+L]
		frequencies = ComputingFrequencies(text,k)
		for index in range(4**k):
			if frequencies[index] >= t:
				Clumps[index] = True
	for i in range(4**k):
		if Clumps[i] == True:
			FrequentPatterns.append(NumberToPattern(i,k))
	return FrequentPatterns

print( ClumpFinding(reference,k,t,L) )
