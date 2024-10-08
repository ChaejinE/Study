import sys

input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

root_node = 1
result = [0] * (N + 1)
visited = [False] * (N + 1)
stk = []
stk.append(root_node)
while stk:
    now = stk.pop()

    visited[now] = True
    for child in A[now]:
        if visited[child]:
            continue
        else:
            stk.append(child)
            result[child] = now

for a in result[2:]:
    print(a)
