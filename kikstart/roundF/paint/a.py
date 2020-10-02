# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq
T = int(sys.stdin.readline())

for t in range(T):
    S,RA,PA,RB,PB,C = map(int,sys.stdin.readline().split())
    RP = sorted(tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(C))) # multi line with multi param
    ret = 0
    #print(RP)
    if (2,2) in RP:
        ret = 0
    elif RB == 2 and PB == 2:
        if C == 2:
            ret = 0
        else:
            ret = 1 - 2 + C #0,-1
    elif RA == 2 and PA == 2:
        if C == 2:
            ret = 0
        else:
            ret = 2 - 1 - C #0,1
    else:
        ret = 3 - 1 - C
    print("Case #{}: {}".format(t+1,ret))
    #print("Case #{}: {}".format(t+1," ".join(map(str,ret))))
