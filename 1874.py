import sys


def input():
  return sys.stdin.readline().rstrip()


op = []
series = []
stack = []
array = []
k = 0

N = int(input())

for i in range(N):
  A = int(input())
  array.append(A)

for i in range(N):

  op.append('+')
  stack.append(i + 1)

  while stack[-1] == array[k]:
    series.append(stack[-1])
    stack.pop()
    op.append('-')
    k += 1
    if k == N:
      break
    elif len(stack) == 0:
      break

if series == array:
  for i in range(len(op)):
    print(op[i])
else:
  print("NO")
