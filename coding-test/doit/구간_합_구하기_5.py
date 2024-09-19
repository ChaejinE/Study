# import time

# start = time.time()

N, M = map(int, input().split())
matrix = [[0] + list(map(int, input().split())) for _ in range(N)]
matrix = [[0] * (N + 1)] + matrix
sum_matrix = [[0] * (N + 1) for _ in range(N + 1)]
query_matrix = [list(map(int, input().split())) for _ in range(M)]

for col in range(1, N + 1):
    sum_matrix[1][col] = sum_matrix[1][col - 1] + matrix[1][col]

for row in range(1, N + 1):
    sum_matrix[row][1] = sum_matrix[row - 1][1] + matrix[row][1]

for i in range(2, N + 1):
    for j in range(2, N + 1):
        sum_matrix[i][j] = matrix[i][j] + sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1]

result = []
for query in query_matrix:
    x_1, y_1, x_2, y_2 = query
    result = sum_matrix[x_2][y_2] - sum_matrix[x_2][y_1 - 1] - sum_matrix[x_1 - 1][y_2] + sum_matrix[x_1 - 1][y_1 - 1]
    print(result)

# print(f"Time : {time.time() - start}")
