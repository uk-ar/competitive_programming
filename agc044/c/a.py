#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = tuple(map(int,sys.stdin.readline().split())) # single line with multi param
# a = tuple(sys.stdin.readline() for _ in range(n)) # multi line with single param
# a = tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)) # multi line with multi param
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# INF = float("inf")
import sys,collections

N = int(sys.stdin.readline())
T = sys.stdin.readline().rstrip()
M = 3**N
p = collections.deque(range(M))
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
t = [int(Base_10_to_n(i,3).translate(str.maketrans({"1":"2","2":"1"})),3) for i in range(M)]
print(t)
for c in T:
    if c == "S":
        :
