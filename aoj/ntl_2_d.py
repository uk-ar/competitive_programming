#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# A = list(map(int,sys.stdin.readline().split()))
# A = [sys.stdin.readline() for _ in range(N)]
# A = [list(map(int,sys.stdin.readline())) for _ in range(N)]
# A = [int(sys.stdin.readline()) for _ in range(N)]
# S = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# l1 = len(text1)
# l2 = len(text2)
# dp = [[float("inf")]*(l1+1) for _ in range(l2+1)]
# for r in range(l2):
#  dp[r][0] = init
# for c in range(l1):
#  dp[0][c] = init
# for r in range(l2):
#     for c in range(l1):
#       dp[r+1][c+1]=dp[r][c]
import sys,bisect,math
from functools import reduce
sys.setrecursionlimit(15000)

import sys,bisect,math
A,B = map(int,sys.stdin.readline().split())
res = A//B
if res < 0 and A%B!=0:
  print(res+1)
  exit()
print(res)
