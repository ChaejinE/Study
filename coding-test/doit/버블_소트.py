import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
result = 0
tmp = [0] * N


def merge_sort(L, start, end):
    global N, result, tmp

    if end - start <= 0:
        return

    m = start + (end - start) // 2
    merge_sort(L, start, m)
    merge_sort(L, m + 1, end)

    for i in range(N):
        tmp[i] = L[i]

    set_idx1 = start
    set_idx2 = m + 1

    i = start
    while set_idx1 <= m and set_idx2 <= end:
        if tmp[set_idx1] < tmp[set_idx2]:
            L[i] = tmp[set_idx1]
            set_idx1 += 1
        else:
            # result += m - set_idx1 + 1  # Length of the left side set (Count num of the swap)
            result += set_idx2 - i  # Length of the left side set (Count num of the swap)
            L[i] = tmp[set_idx2]
            set_idx2 += 1

        i += 1

    while set_idx1 <= m:
        L[i] = tmp[set_idx1]
        set_idx1 += 1
        i += 1

    while set_idx2 <= end:
        L[i] = tmp[set_idx2]
        set_idx2 += 1
        i += 1


merge_sort(A, 0, N - 1)
# print(A)
print(result)
