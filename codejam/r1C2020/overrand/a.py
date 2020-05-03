#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys,math,collections
sys.setrecursionlimit(15000)
def solve():
    u = int(sys.stdin.readline())
    d = collections.defaultdict(int)
    for _ in range(10000):
        q,r = sys.stdin.readline().split() # int,string
        # if q == "-1":
        #     pass
        # elif len(q) > len(r):#2,1
        #     pass
        #elif (len(r) == len(q)):
        d[r[0]] += 1
        if not r[-1] in d:
            d[r[-1]] += 1
    nd = sorted([(value, key) for key, value in d.items()])
    #print(nd)
    ret = [nd[0][1]]
    for i in range(1,10)[::-1]:
        ret.append(nd[i][1])
    return "".join(ret)


T = int(sys.stdin.readline())
for t in range(T):
    res = solve()
    print("Case #{}: {}".format(t+1,res))
