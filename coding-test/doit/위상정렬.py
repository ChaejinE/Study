A = [1, 2, 3, 4, 5]
N = len(A)
T = [[2, 3], [4, 5], [4], [5], []]
indegree = [0] * (N + 1)

A = [0] + A
T = [[]] + T
for i in range(1, N + 1):
    for j in T[i]:
        indegree[j] += 1

from collections import deque

q = deque([])
q.append(A[1])
result = []

while q:
    now = q.popleft()
    result.append(now)

    for i in T[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(result)
