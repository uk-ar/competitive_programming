#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys
sys.setrecursionlimit(15000)

def postfix(ss):
    #postfixs = [s[1:] for s in ss]
    postfixs = [s[s.rfind("*")+1:] for s in ss]
    #print(postfixs)
    longest = max(postfixs, key=len)
    if all(longest.endswith(s) for s in postfixs):
        return longest
    else:
        return None

def prefix(ss):
    #postfixs = [s[1:] for s in ss]
    prefixs = [s[:s.find("*")] for s in ss]
    #print(prefixs)
    longest = max(prefixs, key=len)
    if all(longest.startswith(s) for s in prefixs):
        return longest
    else:
        return None

def middle(ss):
    mids = [s[s.find("*")+1:s.rfind("*")] for s in ss]
    #print(mids)
    return "".join(mid.replace("*","") for mid in mids)

def solve():
    n = int(sys.stdin.readline())
    ss = [sys.stdin.readline().rstrip() for _ in range(n)]
    post = postfix(ss)
    pre = prefix(ss)
    mid = middle(ss)
    if post == None or pre == None:
        res = "*"
    else:
        res = pre + mid + post
    return res


T = int(sys.stdin.readline())
for t in range(T):
    ret = solve()
    print("Case #{}: {}".format(t+1, ret))
