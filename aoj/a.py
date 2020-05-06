#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys

N,W = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

#for sparse data
# 05_large 11s->6s
import collections
dp = {}
dp[0] = 0
a = sorted(a,reverse=True)
for v,w in a:
  temp = dp.copy()
  for j in list(dp.keys()):
    if j+w <= W and (not j+w in dp or dp[j+w] < dp[j]+v):
      temp[j+w] = dp[j]+v
  #dp = {**dp,**temp}
  dp = temp
print(max(dp.values()))

# # naive
# dp = [[0]*(W+1) for _ in range(N)]
# for i in range(N):
#   v,w = a[i]
#   for j in range(W+1):
#     if 0 <= j-w:
#       dp[i][j] = max(dp[i-1][j],dp[i][j-w]+v)
#     else:
#       dp[i][j] = dp[i-1][j]
# #opt mem
# dp = [0]*(W+1)
# for i in range(N):
#   v,w = a[i]
#   for j in range(W+1)[::-1]:
#     if 0 <= j-w: #select
#       dp[j] = max(dp[j],dp[j-w]+v)
#opt
# dp = [0]*(W+1)
# last = 0
# for i in range(N):
#   v,w = a[i]
#   # print(last)
#   # print(dp)
#   last = min(last+w+1, W+1)
#   for j in range(last)[::-1]:
#     if 0 <= j-w and dp[j] <= dp[j-w]+v: #select
#       dp[j] = dp[j-w]+v
