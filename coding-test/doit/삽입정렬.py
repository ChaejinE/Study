N = 5
A = [42, 32, 24, 60, 15]

for i in range(1, N):
    target_insert_value = A[i]

    # search the insert point
    target_insert_idx = i
    for j in range(i):
        if A[i] <= A[j]:
            target_insert_idx = j
            break

    # shift
    for k in range(i, target_insert_idx - 1, -1):
        if k > 0:
            A[k] = A[k - 1]

    A[target_insert_idx] = target_insert_value

print(A)
