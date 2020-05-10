#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect,math
sys.setrecursionlimit(15000)

K = int(sys.stdin.readline())
A,B = map(int,sys.stdin.readline().split())

if A%K == 0 or B%K == 0:
    print("OK")
    exit()
if A//K == B//K:
    print("NG")
    exit()
print("OK")
