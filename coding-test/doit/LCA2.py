import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

M = int(input())
depth = [0] * (N + 1)
root_node = 1
depth[root_node] = 1
tmp = 1
K = 0

while tmp <= N:
    tmp = 2**tmp
    K += 1

parent = [[0] * (N + 1) for _ in range(K + 1)]


def bfs(root):
    q = deque([])
    q.append(root)
    visited = [False] * (N + 1)
    visited[root] = True

    while q:
        now = q.popleft()

        for child in tree[now]:
            if not visited[child]:
                visited[child] = True
                q.append(child)
                parent[0][child] = now
                depth[child] = depth[now] + 1


bfs(root_node)
for k in range(1, K + 1):
    for i in range(1, N + 1):
        parent[k][i] = parent[k - 1][parent[k - 1][i]]


def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    # Make the depth to be same
    for k in range(K, -1, -1):
        if 2**k <= depth[b] - depth[a]:
            if depth[a] <= depth[parent[k][b]]:
                b = parent[k][b]

    # Find LCA fastly
    for k in range(K, -1, -1):
        if a == b:
            break
        elif parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    lca_ = a
    if a != b:
        lca_ = parent[0][lca_]
    return lca_


for _ in range(M):
    node1, node2 = map(int, input().split())
    result = lca(node1, node2)
    print(result)
