#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math,itertools
sys.setrecursionlimit(15000)

N,M,Q = map(int,sys.stdin.readline().split())
qs = [list(map(int,sys.stdin.readline().split())) for _ in range(Q)]
com = list(itertools.combinations_with_replacement(range(1,M+1), N))
m = 0
#print(qs)
#print(com)
for A in com:
    s = 0
    for a,b,c,d in qs:
        if A[b-1] - A[a-1] == c:
            s += d
    m = max(m,s)
print(m)
