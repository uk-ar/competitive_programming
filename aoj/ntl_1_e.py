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

A,B = map(int,sys.stdin.readline().split())

def exgcd0(x,y):
  # if x < y:
  #   x,y = y,x
  a0,b0,r0=1,0,x
  a1,b1,r1=0,1,y
  while r1 > 0:
    q1=r0//r1
    r2=r0%r1
    a2=a0-q1*a1
    b2=b0-q1*b1
    a0,b0,r0=a1,b1,r1
    a1,b1,r1=a2,b2,r2
  return a0,b0,r0#a,b,c

def exgcd(a,b):
  if b==0:
    return 1,0,a
  else:
    q=a//b
    r=a%b
    s1,t1,c = exgcd(b,r)
    s = t1
    t = s1-t1*q
    return s,t,c

ret = exgcd0(A,B)
print(ret[0],ret[1])
