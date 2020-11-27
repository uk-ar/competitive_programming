#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys

N = int(sys.stdin.readline())
a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

left = [0]*(N+1)
for i in range(N):
    left[i+1] = left[i]^a[i]

right = [0]*(N+1)
for i in range(N)[::-1]:
    right[i] = right[i+1]^a[i]

ret = []
for i in range(N):
    ret.append(left[i]^right[i+1])

print(" ".join(map(str,ret)))
