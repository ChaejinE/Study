import heapq

def heap_sort(nums):
    new_nums = [ -x for x in nums ]
    result = [ 0 ] * len(new_nums)
    heapq.heapify(new_nums)
    for i in range(len(new_nums)-1, -1, -1):
        max_num = heapq.heappop(new_nums) * -1
        result[i] = max_num
    return result

if __name__ == "__main__":
    nums = [5,7,9,3,1,5,5,2,4]
    result = heap_sort(nums)
    print(result)