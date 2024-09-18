def counting_sort(nums):
    count_list = [ 0 ] * len(nums)
    accumulated_list = [ 0 ] * len(nums)
    
    for num in nums:
        count_list[num] += 1
    
    accumulated_val = 0
    for idx, count in enumerate(count_list):
        accumulated_val += count
        accumulated_list[idx] = accumulated_val - 1
        
    result = [ 0 ] * len(nums)
    for num in nums[::-1]:
        idx = accumulated_list[num]
        result[idx] = num
        accumulated_list[num] -= 1
        
    return result
    
if __name__ == "__main__":
    nums = [3, 0, 5, 1, 0, 5]
    result = counting_sort(nums)
    
    print(result)