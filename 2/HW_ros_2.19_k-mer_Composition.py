#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')
read_name = file.readline().strip()[1:]
read = ""
for line in file:
	read += line.strip()

def SymbolToNumber(symbol):
	symbols = {"A":0,"C":1,"G":2,"T":3}
	return symbols[symbol]

def PatternToNumber(pattern):
	if pattern == "":
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def ComputingFrequencies(text, k):
	frequencies = [0] * (4**k)
	for i in range(len(text)-k+1):
		frequencies[PatternToNumber( text[i:i+k] )] += 1
	return frequencies

print( ComputingFrequencies(read,4) )
