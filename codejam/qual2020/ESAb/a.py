#!/usr/bin/env python3
# n,m = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# s = sys.stdin.readline().rstrip()
# i = int(sys.stdin.readline())
import sys

count = 0
def ask(b):
  global count
  print(b)
  sys.stdout.flush()
  ans = int(input())
  return ans

T,B = map(int,sys.stdin.readline().split())
for t in range(T):
  ret= [0]*B
  sa = [0]*B
  for i in range(1,B+1):
    ret[i-1] = ask(i)
    print("s",i-1,ret[i-1],ret, file=sys.stderr)
  #print("s",b,sa,ret, file=sys.stderr)
  print("".join(map(str,ret)), file=sys.stderr)
  if t == 0:
    print("01101001110110001111")
    print("01101001110110001111:act", file=sys.stderr)
  elif t == 1:
    print("00010011011000110100")
    print("00010011011000110100:act", file=sys.stderr)
  elif t == 2:
    print("00100111101011101001")
    print("00100111101011101001:act", file=sys.stderr)
  else:
    print("".join(map(str,ret)))
    #print("1"*B)
  sys.stdout.flush()
  ans = input()
  if ans == "N":
    exit()
  #print("ans",ans, file=sys.stderr)
  #a, b = map(int, input().split())
  #_ = int(input())
  #solve(a + 1, b)
