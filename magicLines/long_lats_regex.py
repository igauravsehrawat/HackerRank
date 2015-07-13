import sys
import re

# ****FILL THE MISSING LINE HERE****
digit = "[-+]?[1-9]\d*\.\d+|[-+]?[1-9]\d*"
prog = re.compile("\((" + digit + "), (" + digit + ")\)")

n = int(sys.stdin.readline())

for s in sys.stdin:
    s = s.rstrip('\n')
    result = prog.match(s)
    if result:
        x = float(result.group(1))
        y = float(result.group(2))
        if (-90 <= x and x <= 90
        and -180 <= y and y <= 180):
            print "Valid"
            continue
    print "Invalid"
