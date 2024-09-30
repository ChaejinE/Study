import sys

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
G = [[] for _ in range(V + 1)]  # Graph 인접 리스트
D = [INF] * (V + 1)  # 최단경로 배열
D[K] = 0
visited = [False] * (V + 1)  # 방문 배열

for _ in range(1, E + 1):
    u, v, w = map(int, input().split())
    G[u].append([v, w])

import heapq

pq = []
heapq.heappush(pq, (D[K], K))


def dijkstra():
    while pq:
        weight, now = heapq.heappop(pq)
        if visited[now]:
            continue

        visited[now] = True
        for v, w in G[now]:
            if D[v] > w + weight:
                D[v] = w + weight
                heapq.heappush(pq, (D[v], v))


dijkstra()

for i in range(1, V + 1):
    if D[i] == INF:
        print("INF")
    else:
        print(D[i])
