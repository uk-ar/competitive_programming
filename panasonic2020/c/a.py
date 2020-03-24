#!/usr/bin/env python3
import math
a,b,c = map(int,input().split())
# a + b + 2r(ab) < c
# a + b - c < -2r(ab)
# c - a - b > 2r(ab)
# (c - a - b)**2 > 4ab
if c - a - b > 0 and (c - a - b)**2 > 4*a*b:
    print("Yes")
    exit()
print("No")
