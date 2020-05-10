#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
INF = float("inf")
import sys,collections

N,M,X = map(int,sys.stdin.readline().split())

C = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param

ALL = [0]*(M+1)
for a in C:
    for i in range(M+1):
        ALL[i] += a[i]
#print(ALL,X)
if any(e < X for e in ALL[1:]):
    print(-1)
    exit()

m = INF
def backtrack(n,c):
    #print(n,c)
    if n == N:
        if all(a >= X for a in c[1:]):
            #print("OK",n,c,X)
            global m
            m = min(m,c[0])
        return
    backtrack(n+1,c)#not select
    backtrack(n+1,[a+b for a,b in zip(c,C[n])])#select

backtrack(0,[0]*(M+1))
print(m)
