from re import L
import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()
N = int(input())
deq = deque(enumerate(input()))

for i in range(N):
    p = deq.pop()
    print(p[0])
    if int(p[1]) > 0:
        deq.rotate(int(p[1])-1)
    else:
        deq.rotate(-(int(p[1])-1))