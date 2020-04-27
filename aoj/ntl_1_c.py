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
A = list(map(int,sys.stdin.readline().split()))

def lcm(x,y):
  return x*y // math.gcd(x,y)

print(reduce(lcm,A))
