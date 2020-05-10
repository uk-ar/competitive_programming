#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math,collections
sys.setrecursionlimit(15000)

N,M = map(int,sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))
good = [1]*N

for _ in range(M):
    a,b = list(map(int,sys.stdin.readline().split()))
    if h[a-1] > h[b-1]:
        good[b-1] = 0
    elif h[a-1] < h[b-1]:
        good[a-1] = 0
    else:# h[a-1] == h[b-1]:
        good[a-1] = 0
        good[b-1] = 0
#cprint(good)
print(sum(good))
