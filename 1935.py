gimport sys

def input():
  return sys.stdin.readline().rstrip()
  
N = int(input())
array = input()
array2 = []
dic = {}
oper = '+-*/'
stack = []

#array2로 알파벳만 모음
for i in array:

  if i not in oper:
    array2.append(i)

#dictionary에 A=1, B=2 꼴로 저장
for i in range(N):
  dic[array2[i]] = i+1

for i in array:
  if i not in oper:
    stack.append(dic[i])

  elif i == '+':
    a = stack.pop()
    b = stack.pop()
    stack.append(b + a)  #연산 후에 다시 stack에 append

  elif i == '-':
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)

  elif i == '*':
    a = stack.pop()
    b = stack.pop()
    stack.append(b * a)

  elif i == '/':
    a = stack.pop()
    b = stack.pop()
    stack.append(b / a)

for i in dic.values():
  print(i)

print(stack[0])
