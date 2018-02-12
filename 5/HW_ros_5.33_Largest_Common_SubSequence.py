#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")

X_ = inp.readline().strip()
Y_ = inp.readline().strip()
S_ = {'G': {'G':  5, 'T': -2, 'A': -2, 'C': -2}, 
	  'T': {'G': -2, 'T':  5, 'A': -2, 'C': -2}, 
	  'A': {'G': -2, 'T': -2, 'A':  5, 'C': -2}, 
	  'C': {'G': -2, 'T': -2, 'A': -2, 'C':  5}}
g_ = -3


def longest_subsequence(seq1,seq2):
	subsequence = ""
	return subsequence


def global_viterbi(X, Y, S, g):

    X = "0" + X
    Y = "0" + Y
    scores = [0] * len(X)
    moves  = [0] * len(X)
    for i in range(len(X)):
        scores[i] = [0] * len(Y)
        moves [i] = [""] * len(Y)

    for x in range(len(X)):
        for y in range(len(Y)):
            if( (y==0) & (x==0) ):
                scores[x][y] = 0
                moves [x][y] = 0
            elif ( x==0 ):
                scores[x][y] = scores[x][y-1] + g
                moves [x][y] = "y"
            elif ( y==0 ):
                scores[x][y] = scores[x-1][y] + g
                moves [x][y] = "x"
            else:
                m_y = scores[x]  [y-1] + g
                m_x = scores[x-1][y]   + g
                m_m = scores[x-1][y-1] + S [X[x]] [Y[y]]

                if ((m_y >= m_x) & (m_y >= m_m)):
                    scores[x][y] = m_y
                    moves[x][y] = "y"
                elif ((m_x >= m_y) & (m_x >= m_m)):
                    scores[x][y] = m_x
                    moves[x][y] = "x"
                elif ((m_m >= m_x) & (m_m >= m_y)):
                    scores[x][y] = m_m
                    moves[x][y] = "m"

    path = []

    while (x > 0 ) | (y > 0 ):
        if(moves[x][y] == "m"):
            path.insert(0,[x-1,y-1])
            x -= 1
            y -= 1
        elif(moves[x][y] == "x"):
            x -= 1
        elif(moves[x][y] == "y"):
            y -= 1

    for i in scores:
        print(*i,sep="\t")
    for i in moves:
        print(*i,sep="\t")
    
    for i in range(len(path)):
    	print( X_[path[i][0]], Y_[path[i][1]] )

    return scores, moves, path



print ( global_viterbi(X_,Y_,S_,g_) )
#print(longest_subsequence(seq1,seq2))
