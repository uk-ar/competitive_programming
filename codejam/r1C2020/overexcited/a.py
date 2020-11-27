#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,math,collections
sys.setrecursionlimit(15000)
d = {"S":(0,-1),"N":(0,1),"E":(1,0),"W":(-1,0),"B":(0,0)}
def solve():
    x,y,m = sys.stdin.readline().split()
    x = int(x)
    y = int(y)
    m = "B"+m.rstrip()
    n = len(m)
    #print(x,y)
    for i,c in enumerate(m):
        x += d[c][0]
        y += d[c][1]
        #print(x,y,i)
        if abs(x)+abs(y) <= i:
            return str(i)
    return "IMPOSSIBLE"

T = int(sys.stdin.readline())
for t in range(T):
    res = solve()
    print("Case #{}: {}".format(t+1,res))
