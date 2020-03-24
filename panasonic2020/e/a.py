#!/usr/bin/env pypy
a = input()
b = input()
c = input()
a_n,b_n,c_n=len(a),len(b),len(c)
m = 12000
r = range(-100,100)
import itertools
for c_i, b_i in itertools.product(r, r):
    f = True
    for g_i in range(min([b_i,c_i,0]),max([a_n,b_n+b_i,c_n+c_i])):
        t = None
        if 0 <= g_i and g_i < a_n:
            t = a[g_i]
        if 0 <= g_i-b_i and g_i-b_i < b_n:
            if t != b[g_i-b_i] and t == "?":
                t = b[g_i-b_i]
            elif t != b[g_i-b_i] and b[g_i-b_i] != "?":
                f = False
                break
        if 0 <= g_i-c_i and g_i-c_i < c_n:
            if t != b[g_i-c_i] and b[g_i-c_i] != "?":
                f = False
                break
        if f == True:
            m = min(m,max([a_n,b_n+b_i,c_n+c_i])-min([0,b_i,c_i]))
print(m)
