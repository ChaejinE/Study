import sys

input = sys.stdin.readline
V = int(input())
E = int(input())
INF = sys.maxsize
G = [[INF for j in range(V + 1)] for i in range(V + 1)]
for i in range(V + 1):
    G[i][i] = 0

for _ in range(E):
    s, e, w = list(map(int, input().split()))
    if G[s][e] > w:
        G[s][e] = w

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

for i in range(1, V + 1):
    for j in range(1, V + 1):
        if G[i][j] == INF:
            print(0, end=" ")
        else:
            print(G[i][j], end=" ")
    print()
