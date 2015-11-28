#!/bin/python

def gcd(number1, number2) :
	looper = 1
	gcd_number = 1
	while ((looper <= number1) or (looper <= number2)) :
		if ((number1 % looper == 0) and (number2 % looper ==0)) :
			gcd_number = looper
		looper += 1
	return gcd_number

def main() :
	A,B,C,D = raw_input().strip().split(' ')
	A,B,C,D = [int(A),int(B),int(C),int(D)]
	ghost_count = 0
	for town in xrange(1, A + 1) :
		for street in xrange(1, B + 1) :
			for apartment in xrange(1, C + 1) :
				for house in xrange(1, D + 1) :
					if (abs(town - street) % 3 == 0) :
						if ((street + house) % 5 == 0) :
							if ((town * house) %  4 == 0) :
								if (gcd(town, apartment) == 1) :
									ghost_count += 1
	print ghost_count
	return

if __name__ == "__main__" :
	main()


