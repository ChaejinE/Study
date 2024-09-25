N = 5
A = [42, 32, 24, 60, 15]

for i in range(N):
    for j in range(N - i):
        if j < N - i - 1 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]  # swap

print(A)
