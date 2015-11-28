#!/bin/python

#
# memoization not done
# try catch error
#

def possibilites(NextPossibleDenominations, N) :
	COUNT = 0
	denominations_iter = iter(NextPossibleDenominations)
	denomination = next(denominations_iter)
	next_value_index = 0
	while(N - denomination >= 0) :
		print N
		currentN = N - denomination
		COUNT +=1
		if (currentN == 0) :
			break
		COUNT += possibilites(denominations[next_value_index:], currentN)
		denomination = next(denominations_iter)
		next_value_index += 1
	return COUNT

if __name__ == "__main__" :
	N = int(raw_input().strip())
	denominations = [2, 5, 10, 20, 50, 100]
	result = possibilites(denominations, N)
	print result + 1