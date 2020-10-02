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
N = len(S)
def solve(i,c,s):
    #print(i,c,s)
    if i == N:
        return [s+c]
    ret = []
    ret.extend(solve(i+1,0,s+c*10+int(S[i])))
    ret.extend(solve(i+1,c*10+int(S[i]),s))
    return ret
#print(solve("25"))
print(sum(solve(0,0,0))//2)
#print(sum(solve(S)))
