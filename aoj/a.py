#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
import sys,bisect
sys.setrecursionlimit(15000)
h,w = map(int,sys.stdin.readline().split())
dp = [[0]*w for _ in range(h)]
m = 0
for i in range(h):
  a = list(map(int,sys.stdin.readline().split()))
  for j in range(w):
    if a[j] == 1:
      dp[i][j] = 0
    elif i == 0 or j == 0:
      dp[i][j] = 1
      m = max(m,dp[i][j])
    else:
      dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
      m = max(m,dp[i][j])
print(m*m)
