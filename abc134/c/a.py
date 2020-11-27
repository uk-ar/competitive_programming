#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections
sys.setrecursionlimit(1000000)
INF = float("inf")

N = int(sys.stdin.readline())
A = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param

left=[-INF]*(N+1)
right=[-INF]*(N+1)

for i in range(N):
    left[i+1] = max(left[i],A[i])

for i in range(N)[::-1]:
    right[i] = max(right[i+1],A[i])

for i in range(N):
    print(max(left[max(0,i)],right[min(N,i+1)]))
