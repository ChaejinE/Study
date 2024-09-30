import sys

input = sys.stdin.readline
N, M = map(int, input().split())
edge_list = [()] * (M + 1)
INF = sys.maxsize
distance = [INF] * (N + 1)
distance[1] = 0

for i in range(1, M + 1):
    edge_list[i] = tuple(map(int, input().split()))

is_cycle = False


def update_edge():
    global is_cycle
    for edge in edge_list[1:]:
        s, e, w = edge
        if distance[s] != INF and distance[s] + w < distance[e]:
            distance[e] = distance[s] + w
            is_cycle = True


for _ in range(1, N):
    update_edge()

is_cycle = False
update_edge()

if is_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)
