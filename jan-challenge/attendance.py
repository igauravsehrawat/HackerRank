def main():
    testcases = int(raw_input())
    for test in xrange(0, testcases):
        #refer to problem https://www.hackerrank.com/contests/101hack21/challenges/angry-professor
        nk = raw_input().split(' ')
        n, k = int(nk[0]), int(nk[1])
        student_timings = raw_input().split(' ')
        class_counter = 0
        for itr in xrange(0, n):
            student_timing = int(student_timings[itr])
            if (student_timing) < 0:
                class_counter += 1
                if (class_counter >= k):
                    print "NO"
                    break
            else:
                pass

        if (class_counter < k):
            print "YES"

if __name__ == "__main__":
    main()
