#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# INF = float("inf")
import sys
S = sys.stdin.readline().rstrip()
A,B,C,D = [int(c) for c in S]

def calc(s,i,ops):
    #print(i,s,ops)
    if i == 4:
        if s == 7:
            print(S[0]+ops[0]+S[1]+ops[1]+S[2]+ops[2]+S[3]+"=7")
            exit(0)
        else:
            return
    calc(s+int(S[i]),i+1,ops+["+"])
    calc(s-int(S[i]),i+1,ops+["-"])

calc(int(S[0]),1,[])
