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

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

def isPrime(n):
  if n == 2:
    return True
  for i in range(2,math.ceil(pow(n,0.5))+1):
    if n % i == 0:
      return False
  return True

print(sum(1 for e in A if isPrime(e)))
