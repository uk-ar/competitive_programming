#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
INF = float("inf")
import sys,collections,heapq,math

N,Q = map(int,sys.stdin.readline().split())
c = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
lr = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(Q)) # multi line with multi param

left=[0]*(N+1)
cur = set()
for i in range(N):
    cur.add(c[i])
    left[i+1] = len(cur)

right = [0]*(N+1)
cur = set()
for i in range(N)[::-1]:
    cur.add(c[i])
    right[i] = len(cur)

for l,r in lr:
    l,r = l-1,r-1
    #print(left[l],left[r],right[l],right[r])
    print(left[l],left[r+1],right[l],right[r+1])
    print(max(left[r+1]-left[l],right[l]-right[r+1]))
