import sys
import re

#****FILL THE MISSING LINE HERE****
digit = "\+?-?[0-9]+.?[0-9]+"
prog = re.compile("\((" + digit + "), (" + digit + ")\)\Z")

n = int(sys.stdin.readline())

for s in sys.stdin:
    s = s.rstrip()
    result = prog.match(s)
    if result:
        x = float(result.group(1))
        y = float(result.group(2))
        if (-90 <= x and x<=90
             and -180 <= y and y <= 180):
            print "Valid"
            continue
    print "Invalid"
