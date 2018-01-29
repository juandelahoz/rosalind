#!/usr/bin/python
import sys

file = open(sys.argv[1], 'r')
seqs = file.read().splitlines()

trie = []
initial = seqs[0]
last = 0

for i in range(len(initial)):
    trie.append((i+1,i+2,initial[i]))
    last = i+2

for seq in seqs:
    path = 1
    for i in range(len(seq)):
        in_path = False
        for node in trie:
            if node[0] == path and node[2] == seq[i]:
                path = node[1]
                in_path = True 
                break
        if in_path == False:
            last += 1
            trie.append((path,last,seq[i]))
            path = last

for t in trie:
    print(str(t[0])+" "+str(t[1])+" "+t[2])
