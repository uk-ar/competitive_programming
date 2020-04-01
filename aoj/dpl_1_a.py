#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n,m = map(int,sys.stdin.readline().split())
M = list(map(int,sys.stdin.readline().split()))
dp = [float("inf")]*(n+1)
dp[0] = 0
for e in M:
  for i in range(n+1):
    if 0 <= i-e and i-e < n:
      dp[i] = min(dp[i],dp[i-e]+1)
print(dp[-1])
