#!/usr/bin/python
import sys

file  = open(sys.argv[1],"r")
k,t = map(int, file.readline().strip().split(" "))
dna = []
for line in file:
    dna.append( line.strip() )

def form_profile(motifs):
	profile = []
	for i in range(4):
		profile.append( [1.0] * len(motifs[0]) )
	for motif in motifs:
		for i in range(len(motif)):
			if motif[i] == "A":
				profile[0][i] +=1.0
			elif motif[i] == "C":
				profile[1][i] +=1.0
			elif motif[i] == "G":
				profile[2][i] +=1.0
			elif motif[i] == "T":
				profile[3][i] +=1.0
	tot = len(motifs) +4
	for prof in profile:
		for i in range(len(prof)):
			prof[i] = prof[i] /tot
	return profile

def Score(motifs, profile):
	scores = [1] * len(motifs)
	for j in range(len(motifs)):
		for i in range(len(motifs[0])):
			if motifs[j][i] == "A":
				scores[j] *= profile[0][i]
			elif motifs[j][i] == "C":
				scores[j] *= profile[1][i]
			elif motifs[j][i] == "G":
				scores[j] *= profile[2][i]
			elif motifs[j][i] == "T":
				scores[j] *= profile[3][i]
	# to check if it should be added or multiplied
	score = 0
	for sc in scores:
		score += sc
	return score

BestMotifs = []
Motif = []
# BestMotifs <- motif matrix formed by first k-mers in each string from Dna
for dna_i in dna:
	BestMotifs.append(dna_i[:k])
sc_bm = Score(BestMotifs,form_profile(BestMotifs))

# for each k-mer Motif in the first string from Dna
for j in range(len(dna[0])-k+1):
	Motifs = [dna[0][j:j+k]]
	for i in range(1,t):
		profile = form_profile(Motifs)
		most_prob_p = 0
		for m in range(len(dna[i])-k+1):
			sc = Score([dna[i][m:m+k]], profile)
			if most_prob_p < sc:
				most_prob_p = sc
				most_prob_k = dna[i][m:m+k]
		Motifs.append(most_prob_k)
	profile = form_profile(Motifs)
	sc_m = Score(Motifs, profile)
	#print(Motifs, sc_bm, sc_m)
	if sc_bm < sc_m:
		BestMotifs = Motifs
		sc_bm = sc_m

# return BestMotifs
for i in BestMotifs:
	print(i)



