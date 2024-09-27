A = [3, 7, 13, 15, 23, 35, 38, 41, 46, 49, 55, 67, 68, 72, 77, 86]
N = len(A)
input_target = 55
cnt = 1


def binary_search(L, target):
    global cnt
    length = len(L)
    m = length // 2
    cnt += 1

    if L[m] == target:
        print(f"searched ! in {cnt} count")
        return
    elif L[m] > target:
        binary_search(L[:m], target)
    elif L[m] < target:
        binary_search(L[m:], target)
    else:
        print("can't search")


binary_search(A, input_target)
