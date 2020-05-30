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
def dfs(l=0,lim=1,t=[]):
    global ret
    print(l,lim,t,ret)#4 6 10 11
    b = lim - LEAVES[l] # num node(exclude leaf)
    parent = lim//2
    #print(l,lim)
    if b < 0:#or (l == N and 0 < b):
        return False
    if l == N and (lim//2 <= LEAVES[l] and LEAVES[l] <= lim):
        t.append(LEAVES[l])
        ret = max(ret,sum(t))
        print(ret,t)
        return True
    elif l == N:
        return False
    #print(b)
    for p in range(b+1):
        dfs(l+1,p*2,t+[p+LEAVES[l]])
dfs()
if ret==0:
    print(-1)
    exit()
print(ret)
