#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split()) for _ in range(N))) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())

import sys,collections

# value dp naive
N,W = map(int,sys.stdin.readline().split())
vwm = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N))
vw = []

# value dp opt mem #48s in 02_corner_04
# dp = [0]*(W+1)
# for v,w in vw:
#   for j in range(W+1)[::-1]:
#     if 0 <= j-w: #select
#       dp[j] = max(dp[j],dp[j-w]+v)
#   #print(w,v,dp)
# print(max(dp))
vwm = sorted(vwm,key=lambda e:e[1],reverse=True)
# 5s in 04_rand_large_02
dp = collections.defaultdict(int)
dp[0] = 0
for v,w,m in vwm:
  new = dp.copy()
  for j in dp.keys():
    n = 1
    #print("o:",j,v,w,m)
    while n <= m and j+n*w <= W:
      #print("i:",j,n,m,j+n*w,new[j+n*w],dp[j]+n*v,W)
      if new[j+n*w] < dp[j]+n*v:
        new[j+n*w] = dp[j]+n*v
      n += 1
    #   #print(n)
  dp = new
  #print(dp)
print(max(dp.values()))
