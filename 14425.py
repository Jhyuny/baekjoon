import sys
input = sys.stdin.readline

n, m = map(int,input().split())
array=[]
j = 0

for i in range(n):
    A = input().rstrip()
    array.append(A)

print(array)

for i in range(m):
    B = input().rstrip()
    
    if B in array:
        j = j + 1

print(j)


