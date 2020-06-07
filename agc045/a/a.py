#!/usr/bin/env pypy3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")

import sys,collections,math
sys.setrecursionlimit(1000000)

INF = float("inf")

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
    S = sys.stdin.readline().rstrip()
    def backtrack(i,x):
        if i == N:
            return x==0
        if S[i] == '0':
            if backtrack(i+1,x^int(A[i])) == True or backtrack(i+1,x)==True:
                return True
            else:
                return False
        else:
            if backtrack(i+1,x^int(A[i])) == False or backtrack(i+1,x)==False:
                return False
            else:
                return True

    if backtrack(0,0)==True:
        print("0")
    else:
        print("1")
