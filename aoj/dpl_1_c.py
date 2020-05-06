#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [list(map(int(sys.stdin.readline().split()))) for _ in range(N)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)

N,W = map(int,sys.stdin.readline().split())
vw = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# #naive
# dp = [[0]*(W+1) for _ in range(N)]
# for v,w in vw:
#   for j in range(W+1):
#     if 0 <= j-w:
#       dp[i][j] = max(dp[i-1][j],dp[i][j-w]+v)
#     else:
#       dp[i][j] = dp[i-1][j]
# print(dp[-1][-1])
# mem opt
dp = [0]*(W+1)
for v,w in vw:
  for j in range(W+1):
    if 0 <= j-w:
      dp[j] = max(dp[j],dp[j-w]+v)
print(dp[-1])
