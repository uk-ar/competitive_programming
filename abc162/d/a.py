#!/usr/bin/env pypy3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
# import math
# from functools import reduce
import sys
sys.setrecursionlimit(15000)

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
d = {"R":[],"G":[],"B":[]}
sb = set()
for i in range(n):
    d[s[i]].append(i)
    if s[i]=="B":
        sb.add(i)
s = 0
#s = sum(1 for a in d["R"] for b in d["G"] for c in d["B"] if abs(a-b) != abs(b-c) and abs(a-c) != abs(c-b) and abs(b-a) != abs(a-c))
#s = len(d["R"])*len(d["G"])*len(d["B"])-sum(1 for a in d["R"] for b in d["G"] for c in d["B"] if abs(a-b) == abs(b-c) or abs(a-c) == abs(c-b) or abs(b-a) == abs(a-c))
for a in d["R"]:
    for b in d["G"]:
        s += len(d["B"])
        if 2*b-a in sb:
            s -= 1
        if 2*a-b in sb:
            s -= 1
        if (a+b)%2 == 0 and (a+b)//2 in sb:
            s -= 1
print(s)
