#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

D = int(sys.stdin.readline())
c = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
s = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(D)) # multi line with multi param
t = tuple(int(sys.stdin.readline()) for _ in range(D)) # multi line with single param

sat = 0
last = [0]*26
for d in range(D):
    j = t[d]-1
    sat = sat + s[d][j]
    last[j] = d+1
    sat = sat - sum(c[i]*(d+1-last[i]) for i in range(26))
    print(sat)
