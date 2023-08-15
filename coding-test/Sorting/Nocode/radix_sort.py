import math
def process(num, i):
    result = num
    result = result // math.pow(10, i+1)
    return int(result) % 10
    
def counting_sort(nums, i):
    length_range = max(nums, key=lambda x: process(x, i)) + 1
    count_list = [ 0 ] * length_range
    accumulated_list = [ 0 ] * length_range
    for num in nums:
        idx = process(num, i)
        count_list[idx] += 1
    
    accumulated_val = 0
    for idx, count in enumerate(count_list):
        accumulated_val += count
        accumulated_list[idx] = accumulated_val - 1
        
    result = [ 0 ] * len(nums)
    for num in nums[::-1]:
        numberIdx = process(num, i)
        idx = accumulated_list[numberIdx]
        result[idx] = num
        accumulated_list[numberIdx] -= 1
        
    # print("result : ", result)
    return result

def radix_sort(nums):
    max_digit_length = int(math.log10(max(nums)))
    result = nums
    for i in range(max_digit_length+1):
        result = counting_sort(result, i)
    
    return result

if __name__ == "__main__":
    nums = [391, 582, 50, 924, 134, 8, 192]
    result = radix_sort(nums)
    print(result)