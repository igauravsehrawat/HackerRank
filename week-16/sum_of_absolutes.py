#!/usr/bin/python

def find(l, r, arr) :
    sum = 0
    for i in xrange(l, r + 1) :
        sum = abs(sum + arr[i])
    return sum

def main() :
    n, q = [int(x) for x in raw_input().split(' ')]
    arr = [int(y) for y in raw_input().split(' ')]
    while (q > 0) :
        l, r = [int(z) for z in raw_input().split(' ')]
        # reduce the index by one since problem has index from 1
        s_of_abs = find(l - 1, r - 1, arr)
        if (s_of_abs % 2 == 0) :
            print "Even"
        else :
            print "Odd"
        q = q - 1

if __name__ == "__main__":
    main()
