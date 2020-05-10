#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

N,K = map(int,sys.stdin.readline().split())
s = set(range(1,N+1))
for _ in range(K):
    d = int(sys.stdin.readline())
    a = set(map(int,sys.stdin.readline().split()))
    s = s-a
print(len(s))
