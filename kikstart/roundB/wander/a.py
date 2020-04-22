# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
import sys
import collections
import heapq,math
T = int(sys.stdin.readline())

fd = {}
def comb(n, r):
    #print(n,r)
    if not n in fd:
        fd[n] = math.factorial(n)
    if not n-r in fd:
        fd[n-r] = math.factorial(n-r)
    if not r in fd:
        fd[r] = math.factorial(r)
    return  fd[n] // (fd[n - r] * fd[r])

for t in range(T):
    W,H,L,U,R,D = map(int,sys.stdin.readline().split())
    if W == 1 or H == 1:
        ret = 0.0
    else:
        holes = set([(L,U),(R,D)])
        print(holes)
        for hole in holes:
            pass
        ret = comb(W-1+H-1,W-1)
    print(W,H)
    print("Case #{}: {}".format(t+1,ret))
