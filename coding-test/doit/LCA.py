import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

parent = [0] * (N + 1)
depth = [0] * (N + 1)
visited = [False] * (N + 1)
q = deque([])
root_node = 1


def bfs(root):
    q.append(root)
    visited[root] = True

    while q:
        now = q.popleft()

        for child in tree[now]:
            if not visited[child]:
                visited[child] = True
                q.append(child)
                parent[child] = now
                depth[child] = depth[now] + 1


bfs(root_node)


def lca(a, b):
    # Fix the a to greater depth than b
    if depth[a] < depth[b]:
        a, b = b, a

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


parent[root_node] = root_node
depth[root_node] = 1

M = int(input())
my_dict = {}
for _ in range(M):
    node1, node2 = map(int, input().split())
    if not my_dict.get((node1, node2)):
        my_dict[(node1, node2)] = my_dict[(node2, node1)] = lca(node1, node2)

    print(my_dict[(node1, node2)])
