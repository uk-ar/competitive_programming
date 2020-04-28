#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# A = list(map(int,sys.stdin.readline().split()))
# A = [sys.stdin.readline() for _ in range(N)]
# A = [list(map(int,sys.stdin.readline())) for _ in range(N)]
# A = [int(sys.stdin.readline()) for _ in range(N)]
# S = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
import sys,bisect,math
from functools import reduce
sys.setrecursionlimit(15000)

N = int(sys.stdin.readline())

def phi(N):
  n = N
  s = set()
  for i in range(2,math.floor(pow(N,0.5))+1):
    while n%i==0:
      s.add(i)
      n = n//i
  if n != 1:
    s.add(n)
  a1 = reduce(lambda a,b: a*b,[e-1 for e in s])
  a2 = reduce(lambda a,b: a*b,[e for e in s])
  #print(N,a1,a2)
  return a1*N//a2

print(phi(N))
