#!/Users/juan/anaconda/bin/python

import sys

inp = open(sys.argv[1],"r")

Money = int(inp.readline().strip())
Coins = list(map(int,inp.readline().strip().split(",")))
Coins.reverse()

def GreedyChange(money,coins):
	change = []
	while money > 0:
		for coin in coins:
			if coin <= money:
				change.append(coin)
				money -= coin
				break
	return change

def RecursiveChange(money, coins):
	# recursive end!
	if money == 0:
		return 0
	minNumCoins = float("inf")
	for i in range(len(coins)):
		if money >= coins[i]:
			numCoins = RecursiveChange( money-coins[i] , coins)
			if  minNumCoins > numCoins + 1:
				minNumCoins = numCoins + 1
	return minNumCoins

def DPChange(money, coins):
	minNumCoins = [0]
	for m in range(1,money+1):
		minNumCoins.append(float("inf"))
		for i in range(len(coins)):
			if m >= int(coins[i]):
				if  minNumCoins[m] > minNumCoins[m-coins[i]] +1:
					minNumCoins[m] = minNumCoins[m-coins[i]] +1
	return minNumCoins[money]

print(DPChange(Money,Coins))
