#!/usr/bin/python

generation = 91
life_span = 17

G = [0 for age in range(life_span)]
G[0] = 1

for j in range(1,generation):
	G0 = 0
	for i in range(life_span-1,0,-1):
		G0 += G[i]
		G[i] = G[i-1]
	G[0] = G0
	print("----- generation " + str(j+1) + " -----")
	print(sum(G), G)

print( sum(G) )
