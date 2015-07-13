def main():
    testcases = int(raw_input())
    while(testcases):
        testcases = testcases - 1
        BW = raw_input().split(' ')
        #assigning values
        b, w = int(BW[0]), int(BW[1])
        XYZ = raw_input().split(' ')
        x, y, z = int(XYZ[0]), int(XYZ[1]), int(XYZ[2])
        mod = (x-y) if ((x-y) > 0) else (y-x)
        #check whether exchange is needed or not
        if(mod > z):
            #no equality needed
            less = y if(x > y) else x
            #how much to exchange and add to total gifts need to buy
            diff = (b) if((x-y) > 0) else (w)
            print (less*(b+w)+z*diff)
        else:
            print (b*x+w*y)


if __name__ == "__main__":
    main()
