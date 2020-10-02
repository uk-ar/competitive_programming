# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq
T = int(sys.stdin.readline())

for t in range(T):
    N,Q = map(int,sys.stdin.readline().split())
    a = list(map(int,sys.stdin.readline().split()))
    q = tuple(sys.stdin.readline() for _ in range(Q)) # multi line with single param

    print("Case #{}: {}".format(t+1,0))
