#!/usr/bin/env pypy3
import sys
sys.setrecursionlimit(15000)
s = input()

if s[2] == s[3] and s[4]==s[5]:
    print("Yes")
else:
    print("No")
