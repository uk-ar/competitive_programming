#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
import sys
sys.setrecursionlimit(15000)

s = sys.stdin.readline().rstrip()
if s.find("7") != -1:
    print("Yes")
    exit(0)
print("No")
