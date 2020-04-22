#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
l1 = len(s1)
l2 = len(s2)
dp = [[float("inf")]*l2 for _ in range(l1)]
dp[0][0] = 0

for i in range(l1):
  for j in range(l2):
    if s1[i]==s2[j]:
      dp[i][j] = dp[max(i-1,0)][max(j-1,0)]
    else:
      dp[i][j] = min(dp[max(i-1,0)][j]+1,dp[i][max(j-1,0)]+1,dp[max(i-1,0)][max(j-1,0)]+1)

print(dp[-1][-1])
