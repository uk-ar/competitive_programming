#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

X = int(sys.stdin.readline())
a = 100.0
n = 0
while X > a:
    a *= 1.01
    a = math.floor(a)
    n += 1
print(n)
