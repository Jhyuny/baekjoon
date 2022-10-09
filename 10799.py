import sys

def input():
  return sys.stdin.readline().rstrip()

pieces = []
stack = []
k = 0
array = str(input())

for i in array:

    if i == '(':
        stack.append('(')
        k += 1
    elif i ==')' and array[k-1] =='(':
        stack.pop()
        pieces.append(len(stack))
        k += 1
    else:
        stack.pop()
        pieces.append(1)
        k += 1

print(sum(pieces))
