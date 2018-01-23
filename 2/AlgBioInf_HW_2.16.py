#!/usr/bin/python

import sys

file = open(sys.argv[1], 'r')
correct = []  	# add new sequence every time that two reads match
incorrect = []	# add new sequence every time it doesn't match anything.
reads = []

def HammingDistance( read_inc, read_cor ):
	distance = 0
	for i in range(len(read_inc)):
		if read_inc[i] != read_cor[i]:
			distance += 1
	return distance

def revCompl(read):
	comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
	rev_comp = ""
	for nucl in read:
		rev_comp = comp[nucl] + rev_comp
	return rev_comp

# read file and save all reads in a list
lines = 0
for line in file:
	if line.startswith(">"):
	 	# save previous read: 
	 	if lines > 0:
	 		reads.append(read)
		# start saving new one
		read_name = line.strip()[1:]
		read = ""
		lines += 1
	else:
		read += line.strip()
reads.append(read)
reads.sort()

# classify reads as correct or incorrect
for i in range(len(reads)):
	readf = reads[i]
	readr = revCompl(readf)
	if   readf in correct:
		continue
	elif readr in correct:
		continue
	elif readf in reads[i+1:]:
		correct.append(readf)
	elif readr in reads[i+1:]:
		correct.append(readf)
	else:
		incorrect.append(readf)

# fix incorrect reads
for read_i in incorrect:
	read_ic = revCompl(read_i)
	for read_c in correct:
		if HammingDistance(read_i, read_c) == 1:
			print(read_i + "->" + read_c)
			continue
		elif HammingDistance(read_ic, read_c) == 1:
			print(read_i + "->" + revCompl(read_c))
			continue

