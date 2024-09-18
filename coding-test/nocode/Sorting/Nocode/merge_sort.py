def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    idx1 = 0
    idx2 = 0

    result = []
    while (idx1 < len(left) and idx2 < len(right)):
        # print(f"idx1 : {idx1} ({left}), idx2 : {idx2} ({right})")
        if left[idx1] < right[idx2]:
            result.append(left[idx1])
            idx1 += 1
        else:
            result.append(right[idx2])
            idx2 += 1

        # print(f"result : {result}")

    while (idx1 < len(left)):
        result.append(left[idx1])
        idx1 += 1
    
    while (idx2 < len(right)):
        result.append(right[idx2])
        idx2 += 1

    return result


if __name__ == "__main__":
    nums = [5, 7, 9, 3, 1, 2, 4]
    result = merge_sort(nums)

    print(result)