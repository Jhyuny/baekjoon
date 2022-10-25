import sys
input = sys.stdin.readline

N = int(input())
Array=[]

for i in range(N):
    a = input()
    b = a.split()

    for j in range(N):
        Array.append(b[j])

Array.reverse()
print(Array[N-1])

