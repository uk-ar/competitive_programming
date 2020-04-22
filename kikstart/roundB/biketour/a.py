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
    n = int(sys.stdin.readline())
    hs = list(map(int, sys.stdin.readline().split()))
    m = -float("inf")
    c = 0
    for i in range(1,n-1):
        if hs[i-1] < hs[i] and hs[i] > hs[i+1]:
            c += 1
        #print(i,hs[i],m,c)
    print("Case #{}: {}".format(t+1,c))
