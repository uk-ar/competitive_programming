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


def Base_10_to_n(X, n):
    m = str(X%n)
    if (X//n):
        return Base_10_to_n(X//n-1, n)+m
    return m

print(Base_10_to_n(N-1,26))
