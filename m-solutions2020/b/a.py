#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys
A,B,C = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())

for i in range(K):
    for j in range(K+1-i):
        #print(i,j)
        if A < 2**i*B and 2**i*B < 2**j*C:
            print("Yes")
            exit()
print("No")
#print(i,2**i*B,j,2**j*C)
