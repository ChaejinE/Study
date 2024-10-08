import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edge_list = []

import heapq

for _ in range(E):
    s, e, w = map(int, input().split())
    heapq.heappush(edge_list, (w, s, e))

parent = [i for i in range(V + 1)]


def find(idx):
    root_idx = None
    if idx == parent[idx]:
        root_idx = idx
    else:
        parent[idx] = find(parent[idx])
        root_idx = parent[idx]

    return root_idx


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False


use_edge = 0
cost = 0
while use_edge < V - 1:
    w, s, e = heapq.heappop(edge_list)
    if find(s) != find(e):
        union(s, e)
        cost += w
        use_edge += 1

print(cost)
