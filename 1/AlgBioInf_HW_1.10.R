#!/usr/local/bin/Rscript

gen = 80 # more than 78 produces a wrong answer...???
life = 17

options(scipen=999)
pop = rep(0,life)
pop[1] = 1
Leslie = matrix(0, nrow=life, ncol=life)
Leslie[1,2:life] = 1
for(i in 2:life){
	Leslie[i,i-1] = 1
}

while(gen >1){
	pop = Leslie %*% pop
	gen = gen - 1
	print(paste("----- generation ",gen," -----"))
	print(c(sum(pop),as.vector(pop)))
}

sum(pop)
