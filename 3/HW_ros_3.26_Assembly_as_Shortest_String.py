#!/usr/bin/python
import sys

file  = open(sys.argv[1],"r")
seqs = []
for line in file:
	if not line.startswith(">"):
		seqs.append( line.strip() )

# initialize variables, start assembling with first read
assembly = seqs[0]
seqs.remove(assembly)

def extend_assembly_shortest(assembly, seqs):
	next_move = ("",len(assembly),"XX")
	for seq in seqs:
		# at least half of the sequence overlaps
		half = int(len(seq)/2)
		for i in range(half,len(seq)):
		# check if as sufix is shorter
			if assembly[-i:] == seq[:i]:
				addition = len(seq) - i
				if next_move[1] > addition:
					next_move = (seq, addition, "sx")
		# check if as prefix is shorter
			if assembly[:i] == seq[-i:]:
				addition = len(seq) - i
				if next_move[1] > addition:
					next_move = (seq, addition, "px")
				
	if next_move[2] == "sx":
		assembly = assembly + next_move[0][-next_move[1]:]
	elif next_move[2] == "px":
		assembly = next_move[0][:next_move[1]] + assembly
	seqs.remove(next_move[0])
	return assembly,seqs

for i in range(len(seqs)):
	assembly,seqs = extend_assembly_shortest(assembly, seqs)

print(assembly)
