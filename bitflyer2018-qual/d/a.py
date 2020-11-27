#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

H,W = map(int,sys.stdin.readline().split())
N,M = map(int,sys.stdin.readline().split())
A = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param

imos=[[0]*(H+1) for _ in range(W+1)]

#https://imoz.jp/algorithms/imos_method.html
for i in range(N):
    for j in range(M):
        if A[i][j] == "#":
            imos[i][j] += 1
            if j
            imos[i][j+M] -= 1

#print(imos)
s = set()
ret = 0
for i in range(M):
    for c in range(C+1):
        imos[c][i+1] += imos[c][i]
    ret = max(ret,sum(min(1,imos[c][i+1]) for c in range(C+1)))
#print(imos)
print(ret)
