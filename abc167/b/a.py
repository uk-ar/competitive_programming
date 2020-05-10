#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

A,B,C,K = map(int,sys.stdin.readline().split())

#ALL = [1]*A+[0]*B+[-1]*C
#print(sum(ALL[:K]))
print(1*min(A,K)+0*min(B,max(K-A,0))-1*min(C,max(K-A-B,0)))
