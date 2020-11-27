#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B
import sys,collections
sys.setrecursionlimit(1000000)
INF = float("inf")

N = int(sys.stdin.readline())
D = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
Q = int(sys.stdin.readline())
P = tuple(int(sys.stdin.readline()) for _ in range(Q)) # multi line with single param

cum = [[0]*(N+1) for _ in range(N+1)]
for r in range(N):
    for c in range(N):
        cum[r+1][c+1] = cum[r+1][c]+D[r][c]
    for c in range(N):
        cum[r+1][c+1] = cum[r][c+1]+cum[r+1][c+1]

dp = [0]*(N*N+1)
for x1 in range(N+1):
    for x0 in range(x1):
        for y1 in range(N+1):
            for y0 in range(y1):
                area = (x1-x0)*(y1-y0)
                dp[area] = max(dp[area],cum[x1][y1]-cum[x0][y1]-cum[x1][y0]+cum[x0][y0])
m = 0
for i in range(N*N+1):
    m = max(m,dp[i])
    dp[i] = m
for i in P:
    print(dp[i])
