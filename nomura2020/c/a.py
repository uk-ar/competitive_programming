#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

N = int(sys.stdin.readline())
LEAVES = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
ret = 0
t = 0
com = []
for l in LEAVES[::-1]:
    t = l + t
    com.append(t)
com.reverse()

def dfs(l=1,parentB=1,t=[]):
    global ret
    lo = parentB-LEAVES[l]
    hi = 2*parentB-LEAVES[l]
    if parentB > com[l]:
        return False
    if l == N and lo <= 0 and 0 <= hi:
        t.append(LEAVES[l])
        ret = max(ret,sum(t))
        print(t,ret)
        return
    elif l == N:
        return
    # #print(b)
    for p in range(lo,hi+1)[::-1]:
        dfs(l+1,p,t+[p+LEAVES[l]])
dfs()
if ret==0:
    print(-1)
    exit()
print(ret)
