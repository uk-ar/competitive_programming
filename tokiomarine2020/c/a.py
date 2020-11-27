#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,math
sys.setrecursionlimit(1000000)

N,K = map(int,sys.stdin.readline().split())
A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

b = [0]*N

print(A)
for i in range(N):
    l = max(i-A[i],0)
    r = min(i+A[i],N-1)
    b[l] += 1
    if r+1 < N: b[r+1] -= 1

for i in range(1,N):
    b[i] += b[i-1]

print(b)
