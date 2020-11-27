#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
# sys.setrecursionlimit(10000)
import sys,collections,math
sys.setrecursionlimit(100000)
a,b = sys.stdin.readline().split()
a = int(a)
b = float(b)
b = int(b*1000)
print(a*b//1000)
