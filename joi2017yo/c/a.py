#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections,math,fractions
sys.setrecursionlimit(1000000)
INF = float("inf")

N,M,D = map(int,sys.stdin.readline().split())
a = tuple(tuple(list(sys.stdin.readline())) for _ in range(N)) # multi line with multi param
#print(a)

dp = [[0]*M for _ in range(N)]
ret = 0
for r in range(N):
    for c in range(M):
        if a[r][c] == "#":
            dp[r][c] = 0
        else:
            dp[r][c] = dp[r][c-1]+1
        if D <= dp[r][c]:
            ret += 1
#print(dp,ret)
for c in range(M):
    dp[-1][c] = 0
for c in range(M):
    for r in range(N):
        if a[r][c] == "#":
            dp[r][c] = 0
        else:
            dp[r][c] = dp[r-1][c]+1
        if D <= dp[r][c]:
            ret += 1
print(ret)
