#!/usr/bin/env python3
'''In this question we need to find the maximum profit in the stock market. in order to solve this question, we need to make two arrays where we will store the 
two different list where we will store the minimum cost and maximum proft.

In this question, i have used dynamic programming.

here we start '''

stock_prices=[8,1,2,4,6,3]
min_cost=[]
max_profit=[]
full_profit=-99999

min_cost.append(stock_prices[0])
for i in range(1,len(stock_prices)):
	min_cost.append(min(min_cost[i-1],stock_prices[i]))
for i in range(len(min_cost)-1):
	max_profit.append(stock_prices[i]-min_cost[i])
	if(max_profit[i]>full_profit):
		full_profit=max_profit[i]




print(full_profit)
