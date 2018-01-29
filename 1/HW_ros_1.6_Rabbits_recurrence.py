#!/usr/bin/python

generation = 36
offspring = 5

def fibonacci( offspring, generation):
	Fn2 = Fn1 = 1
	while generation>2:
		Fn = Fn1 + (Fn2*offspring)
		Fn2,Fn1 = Fn1,Fn
		generation -= 1
	return Fn


print( fibonacci( offspring, generation) )
