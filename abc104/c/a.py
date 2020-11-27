#!/usr/bin/env python3
# N,M = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(int(sys.stdin.readline()) for _ in range(N)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
INF = float("inf")
import sys

D,G = map(int,sys.stdin.readline().split())
pc = tuple(list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(D)) # multi line with multi param

s = sum(p for p,c in pc)
print(s)
# def backtrack(i,t):
#     #print(i,t,pc)
#     if i == s:
#         return INF
#     if t >= G:
#         return i
#     ret = INF
#     for j in range(D):
#         if pc[j][0] > 0:
#             pc[j][0] -= 1
#             if pc[j][0] == 0:
#                 ret = min(ret,backtrack(i+1,t+(j+1)*100+pc[j][1]))
#             elif pc[j][0] > 0:
#                 ret = min(ret,backtrack(i+1,t+(j+1)*100))
#             pc[j][0] += 1
#     return ret
# print(backtrack(0,0))
