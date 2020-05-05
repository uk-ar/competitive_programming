#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
INF = float("inf")
import sys,bisect
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]

# naive O(n**2)
# dp = [0]*n
# for i in range(n):
#   m = 0
#   for j in range(0,i):
#     if a[j] < a[i] and m <= dp[j]:
#       m = dp[j]
#   dp[i] = m+1
# print(max(dp))
import bisect
dp = [float("inf")]*n
dp[0] = a[0]
last = 0
for i in range(1,n):
  if dp[last] < a[i]:
    last += 1
    dp[last] = a[i]
  else:
    j = bisect.bisect_left(dp,a[i])
    dp[j] = a[i]
print(bisect.bisect_left(dp,float("inf")))
