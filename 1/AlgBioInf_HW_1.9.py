#!/usr/bin/python

k,n,m = 15.0,15.0,16.0
tot = k + n + m

if(k>0):
	Pk = k/tot
else:
	Pk = 0
if(n>0):
	Pn = n/tot
else:
	Pn = 0
if(m>0):
	Pm = m/tot
else:
	Pm = 0

if(k>1):
	Pkk = Pk * ((k-1)/(tot-1))
	Pmk = Pm * (k/tot-1)
	Pnk = Pn * (k/tot-1)
else:
	Pkk = 0
	Pmk = 0
	Pnk = 0

if(m>1):
	Pmm = Pm * ((m-1)/(tot-1))
	Pnm = Pn * (m/(tot-1))
	Pkm = Pk * (m/tot-1)
else:
	Pmm = 0
	Pnm = 0
	Pkm = 0

if(n>1):
	Pnn = Pn * ((n-1)/(tot-1))
	Pmn = Pm * (n/(tot-1))
	Pkn = Pk * (n/tot-1)
else:
	Pnn = 0
	Pmn = 0
	Pkn = 0

print(1 - ((Pnn*0.25) + (Pnm*0.5) + (Pmn*0.5) + Pmm))
