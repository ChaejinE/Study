import random

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    last_idx = len(nums)-1
    pivot_idx = random.randint(0, last_idx)
    # print(f"nums : {nums}")
    # print(f"pivotIdx : {pivot_idx}({nums[pivot_idx]})")
    
    ## swap last index, pivot idx value change
    nums[last_idx], nums[pivot_idx] = nums[pivot_idx], nums[last_idx]
    pivot_idx = last_idx
    
    idx1 = 0
    idx2 = last_idx-1 if last_idx-1 >= 0 else 0
    
    while (idx1 <= idx2):
        while (idx1 <= last_idx and nums[idx1] < nums[pivot_idx]):
            idx1 += 1
        while (idx2 >= 0 and nums[idx2] >= nums[pivot_idx]):
            idx2 -= 1
        
        if (idx1 <= idx2):
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
        # print(f"length : {len(nums)}, {nums}, idx1 : {idx1}, idx2 : {idx2}")
    
    ## swap and pivot idx value change 
    nums[idx1], nums[pivot_idx] = nums[pivot_idx], nums[idx1]
    pivot_idx = idx1
    
    # print(f"result :    {nums}")
    return quick_sort(nums[:pivot_idx]) + [ nums[pivot_idx] ] + quick_sort(nums[pivot_idx+1:])
        

if __name__ == "__main__":
    nums = [5,7,9,3,1,5,5,2,4]
    result = quick_sort(nums)
    
    print(result)