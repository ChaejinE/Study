A = [16, 80, 18, 77, 3, 24, 88, 23]
N = len(A)

from collections import deque

my_range = 10
q_list = [deque([]) for _ in range(my_range)]

location_num = len(str(A[0]))
standard = 10

for k in range(location_num):
    for i in range(N):
        if k == 0:
            q_list[A[i] % standard].append(A[i])
        else:
            q_list[A[i] // standard].append(A[i])
            if k > 2:
                standard *= 10

    idx = 0
    for i in range(my_range):
        while q_list[i]:
            A[idx] = q_list[i].popleft()
            idx += 1

print(A)
