#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for _ in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys,bisect
sys.setrecursionlimit(15000)

A,B,C,D = map(int,sys.stdin.readline().split())

if (C+B-1)//B <= (A+D-1)//D:
    print("Yes")
    exit()
print("No")
