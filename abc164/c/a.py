#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
a = [sys.stdin.readline() for _ in range(n)]

import collections
c = collections.Counter(a)
print(len(c))
