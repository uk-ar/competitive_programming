#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
INF = float("inf")
import sys

N,D = map(int,sys.stdin.readline().split())
XY = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
ret = 0
for x,y in XY:
    if x**2 + y**2 <= D**2:
        ret += 1
print(ret)
