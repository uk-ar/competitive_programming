#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys
from functools import reduce
N,K = map(int,sys.stdin.readline().split())

A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param

#pre = reduce((lambda x, y: x * y), [A[i] for i in range(K)])
for i in range(K,N):
    #print(i)
    # cur = (pre//A[i-K])*A[i]
    if A[i-K] < A[i]:
        print("Yes")
    else:
        print("No")
    # if pre < cur:
    #
    # else:
    #     print("No")
    # pre = cur
