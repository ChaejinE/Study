N = 5
A = [42, 32, 24, 60, 15]

for i in range(N):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]  # swap

print(A)
