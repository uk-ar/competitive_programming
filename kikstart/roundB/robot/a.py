# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# r = set(map(str,range(1,10)))
import sys
import collections
import heapq
T = int(sys.stdin.readline())
lim = 1000000000
r = set(map(str,range(1,10)))
def parse(s,i):
    c = 0
    x = y = 0
    while i < len(s):
        #print(i,s[i],x,y)
        if s[i] in r:
            c = int(s[i])
            x0,y0,i = parse(s,i+1)
            #ret += s0*c
            x += x0*c
            y += y0*c
        elif s[i] == ")":
            return x,y,i
        elif s[i] == "(":
            pass
        else:
            #ret.append(s[i])
            if s[i] == "S":
                y += 1
            elif s[i] == "N":
                y -= 1
            elif s[i] == "E":
                x += 1
            elif s[i] == "W":
                x -= 1
        i += 1
    return x,y,i
for t in range(T):
    s = sys.stdin.readline().rstrip()
    # x = 1
    # y = 1
    x,y,_ = parse(s,0)
    x += 1
    y += 1
    #s = "".join(s)
    # for c in s:
    #     if c == "S":
    #         y += 1
    #     elif c == "N":
    #         y -= 1
    #     elif c == "E":
    #         x += 1
    #     elif c == "W":
    #         x -= 1
    if x == 0:
        x = lim
    else:
        x = (x + lim)%lim
    if y == 0:
        y = lim
    else:
        y = (y + lim)%lim
    print("Case #{}: {} {}".format(t+1,x,y))
