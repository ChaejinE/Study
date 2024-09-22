import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
stk = []
result = [0] * N

for i in range(N):
    while stk and A[stk[-1]] < A[i]:
        result[stk.pop()] = A[i]

    stk.append(i)

while stk:
    result[stk.pop()] = -1

for elem in result:
    print(elem, end=" ")
