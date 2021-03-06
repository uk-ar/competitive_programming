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

A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

cur = 1000
for i in range(N-1):
    if A[i] < A[i+1]:
        cur = (A[i+1]-A[i])*(cur//A[i])+cur
    #print(i,cur)
print(cur)
