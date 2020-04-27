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

M,N = map(int,sys.stdin.readline().split())

def powmod(m,n,mod):
  if n == 1:
    return m
  ret = (powmod(m,n//2,mod))%mod
  if n%2==1:
    return (ret*ret*m)%mod
  return ret*ret%mod

print(powmod(M,N,1000000007))
