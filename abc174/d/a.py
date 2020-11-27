#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
INF = float("inf")
import sys,collections

N = int(sys.stdin.readline())
c = sys.stdin.readline().rstrip()
co = collections.Counter(c)
if not "R" in co or not "W" in co:
    print(0)
    exit()
ret = 0
for i in range(co["R"]):
    if c[i] != "R":
        ret += 1
print(ret)
