#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
sys.setrecursionlimit(1000000)
INF = float("inf")

H,W,Q = map(int,sys.stdin.readline().split())
a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
b = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
q = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param

cum = [[0]*(W+1) for _ in range(H+1)]
base = [0]*(W+1)

sign = 1
for c in range(W):
    base[c+1] += base[c]+sign*b[c]
    sign *= -1

sign = 1
for r in range(H):
    for c in range(W+1):
        cum[r+1][c] += cum[r][c]+sign*base[c]*a[r]
    sign *= -1

for px,py,qx,qy in q:
    print(cum[qx][qy]-cum[px-1][qy]-cum[qx][py-1]+cum[px-1][py-1])
