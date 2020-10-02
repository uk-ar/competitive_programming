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
    N,K = map(int,sys.stdin.readline().split())
    se = sorted(tuple(tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N))) # multi line with multi param
    # n log n
    r = []
    for s,e in se:
        if not r:
            r = [[s,e]]
        else:
            if s <= r[-1][1]:
                r[-1][1] = max(r[-1][1],e)
            else:
                r.append([s,e])
    r.reverse()
    #print(r)
    ret = 0
    te = [0,0]
    while r:
        s,e = r.pop()
        #print(te,ret,e)
        if te[1] < e:
            ret += 1
            te = [max(s,te[1]),max(s,te[1])+K]
            #print("s,te:",s,te[1])
            if te[1] < e:
                r.append([s,e])
    print("Case #{}: {}".format(t+1,ret))
    #print("Case #{}: {}".format(t+1," ".join(map(str,ret))))
