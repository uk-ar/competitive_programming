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
dp = [[float("inf")]*(l2+1) for _ in range(l1+1)]
dp[0] = list(range(l2+1))

for i in range(l1):
  dp[i][0] = i
  for j in range(l2):
    if s1[i]==s2[j]:
      dp[i+1][j+1] = dp[i][j]
    else:
      dp[i+1][j+1] = min(dp[i+1][j]+1,
                         dp[i][j+1]+1,
                         dp[i][j]+1)

#print(dp)
print(dp[-1][-1])
