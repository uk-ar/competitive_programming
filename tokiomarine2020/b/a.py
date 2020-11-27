#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/all/DSL_1_B
import sys
sys.setrecursionlimit(1000000)

A,V = map(int,sys.stdin.readline().split())
B,W = map(int,sys.stdin.readline().split())
T = int(sys.stdin.readline().rstrip())

if A==B:
    print("YES")
    exit()
if W-V>=0:
    print("NO")
    exit()
if abs(A-B)/(V-W)<=T:
    #print(abs(A-B)/(V-W))
    print("YES")
    exit()
print("NO")
