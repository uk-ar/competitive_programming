#!/usr/bin/env python3
import sys
sys.setrecursionlimit(15000)
n,w = map(int,sys.stdin.readline().split())
dp = [0]*(w+1)
for i in range(n):
  vi,wi = map(int,sys.stdin.readline().split())
  for j in range(w+1)[::-1]:
    if 0 <= j-wi and j-wi <= w:
      #print(j-wi,vi)
      dp[j] = max(dp[j],dp[j-wi]+vi)
print(dp[-1])
