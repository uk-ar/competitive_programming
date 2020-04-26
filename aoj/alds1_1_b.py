#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# A = list(map(int,sys.stdin.readline().split()))
# A = [sys.stdin.readline() for _ in range(N)]
# A = [list(map(int,sys.stdin.readline())) for _ in range(N)]
# A = [int(sys.stdin.readline()) for _ in range(N)]
# S = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

X,Y = map(int,sys.stdin.readline().split())
def gcd(x,y):
  if x > y:
    x,y = y,x
  if y%x==0:
    return x
  return gcd(x,y%x)

print(gcd(X,Y))
