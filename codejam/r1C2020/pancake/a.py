#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,math,collections
sys.setrecursionlimit(15000)
d = {"S":(0,-1),"N":(0,1),"E":(1,0),"W":(-1,0),"B":(0,0)}
def solve():
    N,D = map(int,sys.stdin.readline().split())
    #a = [sys.stdin.readline() for _ in range(N)]
    a = list(map(int,sys.stdin.readline().split()))
    #print(N,D,a)
    if N == 1:
        return D-1
    c = collections.Counter(a)
    if c.most_common()[0][1] >= D:
        return 0
    if D == 2:
        return 1
    if D == 3:
        d = set()
        for e in a:#koubaisuu
            #print(d,e)
            if e in d:
                return 1
            else:
                d.add(e*2)
                if e%2==0:
                    d.add(e//2)
        if c.most_common()[0][1] == 2:
            if min([k for k,v in c.most_common() if v >= 2]) < max(a):
                return 1
        return 2

T = int(sys.stdin.readline())
for t in range(T):
    res = solve()
    print("Case #{}: {}".format(t+1,res))
