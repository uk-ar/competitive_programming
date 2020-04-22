#!/usr/bin/env pypy3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# a = [sys.stdin.readline() for s in range(n)]
# s = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# d = collections.defaultdict(list)
# h = list() heapify(h)
# sys.stdout.flush()
# print("s",s, file=sys.stderr)
# product('ABCD', repeat=2)# AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)  # AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)  # AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2) #AA AB AC AD BB BC BD CC CD DD
# import math,collections
#def eprint(*args, **kwargs):
#    print(*args, file=sys.stderr, **kwargs)
# def search_x(ng,ok,y):
#     print("sx",ng,ok,y,file=sys.stderr)
#     while abs(ok - ng) > 1:
#         mid = (ok+ng)//2
#         print("o,n,m",ok,ng,mid,file=sys.stderr)
#         ans = ask(mid,y)
#         if ans == "HIT":
#             ok = mid
#         else:
#             ng = mid
#     return ok
import sys
sys.setrecursionlimit(15000)

def eprint(*args, **kwargs):
   print(*args, file=sys.stderr, **kwargs)

def ask(x,y):
  print(x,y)
  sys.stdout.flush()
  s = sys.stdin.readline().rstrip()
  #print("s",s,x,y, file=sys.stderr)
  if s == 'WRONG':
      exit()
  return s

T,A,B = map(int,sys.stdin.readline().split())
print("T,A,B",T,A,B, file=sys.stderr)
lim = 1000000000
def search_hit():
    r = c = 1
    for r in range(1,lim//A+2):
        for c in range(1,lim//A+2):
            eprint(r,c,-lim+r*A,lim-c*A)
            ans = ask(-lim+r*A,lim-c*A)
            if ans == "MISS":
                continue
            else:
                return ans,-lim+r*A,lim-c*A

def search_x(ng,ok,y):
    print("sx",ng,ok,y,file=sys.stderr)
    while abs(ok - ng) > 1:
        mid = (ok+ng)//2
        #print("o,n,m",ok,ng,mid,file=sys.stderr)
        ans = ask(mid,y)
        if ans == "HIT":
            ok = mid
        else:
            ng = mid
    return ok

def search_y(ng,ok,x):
    print("sy",ng,ok,x,file=sys.stderr)
    while abs(ng - ok) > 1:
        mid = (ng+ok)//2
        ans = ask(x,mid)
        if ans == "HIT":
            ok = mid
        else:
            ng = mid
    return ok

def search_center(x,y):
    print("search center",x,y, file=sys.stderr)
    r = c = 1
    x0 = search_x(max(-lim-1,x-2*B),x,y)
    x1 = search_x(min(lim+1,x+2*B),x,y)
    x = (x0+x1)//2
    eprint("x:",x0,x1,x)
    y1 = search_y(max(-lim-1,y-2*B),y,x)
    y0 = search_y(min(lim+1,y+2*B),y,x)
    y = (y0+y1)//2

    eprint("y:",y0,y1,y)
    eprint("x,y:",x,y)
    return ask(x,y),x,y
    # for r in range(-10,11):
    #     for c in range(-10,11):
    #         ans = ask(x+c,y+r)
    #         if ans == "HIT":
    #             continue
    #         else:
    #             return ans,x,y

for t in range(T):
    eprint("test:",t)
    #search hit
    ans,x,y = search_hit()
    eprint("HIT:",ans,x,y)
    if ans == "CENTER":
        eprint("HIT:",ans,x,y)
        continue
    #search center
    ans,x,y = search_center(x,y)
    if ans == "CENTER":
        eprint("CENT:",ans,x,y)
        continue

    # ans = ask(-100000,100000)
    # ans = ask(-10000,10000)
    # ans = ask(-1001,1001)
    # ans = ask(-1000,1000)
    # ans = ask(0,1)
    # ans = ask(0,0)#cent
    # ans = ask(-1,3)#hit
    # ans = ask(-1234567890,1234567890)
    #print("Case #{}: {}".format(t+1,ret))
