A = [42, 32, 24, 60, 15, 5, 90, 45]
N = len(A)
count = 0


# 0  1  2  3  4  5 6
# 42 32 24 50 15 5 90
def quick_sort(L):
    global N

    if len(L) <= 1:
        return []

    pivot_idx = len(L) - 1
    l_idx = 0
    r_idx = len(L) - 2
    while l_idx < r_idx:
        # search lower
        while l_idx < N - 1 and L[l_idx] <= L[pivot_idx]:
            l_idx += 1

        # search greater
        while r_idx > 0 and L[r_idx] >= L[pivot_idx]:
            r_idx -= 1

        if l_idx < r_idx:
            # swap
            L[l_idx], L[r_idx] = L[r_idx], L[l_idx]

        l_idx += 1
        r_idx -= 1

    m = l_idx + 1 if L[l_idx] < L[pivot_idx] else l_idx
    return quick_sort(L[0:m]) + [L[pivot_idx]] + quick_sort(L[m : N - 1])


print(quick_sort(A))
