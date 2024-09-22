import sys

input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))

from collections import deque

dq = deque([])

for i in range(N):
    while dq and dq[-1][1] > A[i]:
        dq.pop()

    dq.append((i, A[i]))

    if i - dq[0][0] + 1 > L:
        dq.popleft()

    print(dq[0][1], end=" ")
