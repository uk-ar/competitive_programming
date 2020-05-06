#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split()))
# a = tuple(sys.stdin.readline() for _ in range(n))
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys

#weight dp ()
def solve1():
  N,W = map(int,sys.stdin.readline().split())
  vw = tuple(tuple(map(int,sys.stdin.readline().split())) for _ in range(N))
  V = sum(v for v,_ in vw)
  dp = [W+1]*(V+1)
  dp[0] = 0
  for v,w in vw:
    for c_v in range(V+1)[::-1]:
      if 0 <= c_v-v: #select
        dp[c_v] = min(dp[c_v],dp[c_v-v]+w)
    #print(dp)
  for c_v in range(V+1)[::-1]:
    if dp[c_v] <= W:
      return c_v
  return V
print(solve1())
