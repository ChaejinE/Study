query = [[], [2, 3], [5, 6], [4], [6], [], []]
N = len(query)


def dfs(visit_list: list, stk: list, A: list):
    while stk:
        crnt = stk.pop()
        print(crnt, end=" ")
        for idx in A[crnt]:
            if not visit_list[idx]:
                stk.append(idx)
                visit_list[idx] = True


start = 1

stack = []
stack.append(start)
visit = [False] * (N + 1)
visit[start] = True
print("DFS :")
dfs(visit, stack, query)
print()

from collections import deque


def bfs(visit_list: list, q: deque, A: list):
    while q:
        crnt = q.popleft()
        print(crnt, end=" ")

        for idx in A[crnt]:
            if not visit_list[idx]:
                q.append(idx)
                visit_list[idx] = True


q = deque([])
q.append(start)
visit = [False] * (N + 1)
visit[start] = True
print("BFS :")
bfs(visit, q, query)
