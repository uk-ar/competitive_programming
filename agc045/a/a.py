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
    a = []
    b = []
    n_0 = 0
    ab=0
    bb=0
    for i in range(N):
        if S[i] == '0':
            a.append(A[i])
            n_0+=1
            ab = A[i]|ab
        else:
            b.append(A[i])
            bb = A[i]|bb
    #print(S,A)
    if (ab & bb) != bb:
        print('1')
        continue
    S=['1']*(N-n_0)+['0']*n_0
    A=b+a
    #print(S,A)
    def backtrack(i,x):
        if i == N:
            return x==0
        if S[i] == '0':
            if x == 0:
                return True
            if backtrack(i+1,x^int(A[i])) == False and backtrack(i+1,x) == False:
                return False
            else:
                return True
        else:
            if backtrack(i+1,x^int(A[i])) == True and backtrack(i+1,x)==True:
                return True
            else:
            #if backtrack(i+1,x^int(A[i])) == False or backtrack(i+1,x)==False:
                return False

    if backtrack(0,0)==True:
        print("0")
    else:
        print("1")
