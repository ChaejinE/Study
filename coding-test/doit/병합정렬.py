L = [42, 32, 24, 60, 15, 5, 90, 45]
N = len(L)


def merge_sort(A, start, end):
    if end - start < 1:
        return

    m = (start + end) // 2

    merge_sort(A, start, m)
    merge_sort(A, m + 1, end)

    set1_idx = start
    set2_idx = m + 1
    tmp = [-1] * N
    tmp_idx = start
    while set1_idx <= m and set2_idx <= end:
        if A[set1_idx] < A[set2_idx]:
            tmp[tmp_idx] = A[set1_idx]
            set1_idx += 1
        else:
            tmp[tmp_idx] = A[set2_idx]
            set2_idx += 1

        tmp_idx += 1

    while set1_idx <= m:
        tmp[tmp_idx] = A[set1_idx]
        set1_idx += 1
        tmp_idx += 1

    while set2_idx <= end:
        tmp[tmp_idx] = A[set2_idx]
        set2_idx += 1
        tmp_idx += 1

    for i in range(start, end + 1):
        A[i] = tmp[i]


merge_sort(L, 0, N - 1)
print(L)
