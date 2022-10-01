###general binary search

def binary_search(lo,hi,condition):
    
    while lo <= hi:
        mid = (lo+hi)//2
        result = condition(mid)

        if result == 'found':
            return mid
        
        elif result == 'left':
            hi = mid-1
            
        elif result == 'right':
            lo = mid+1
    
    return -1


## calculating starting position of the given number using general binary search 

def start_position(nums,target):
    
    def condition(mid):
        mid_num = nums[mid]
        
        if mid_num == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            else:
                return 'found'
            
        elif mid_num > target:
            return 'left'
        
        elif mid_num < target:
            return 'right'   
    
    return binary_search(0,len(nums)-1,condition)


## calculating ending position of the given number using general binary search 

def end_position(nums,target):
    
    def condition(mid):
        mid_num = nums[mid]
        
        if mid_num == target:
            if mid < (len(nums)-1) and nums[mid+1] == target:
                return 'right'
            else:
                return 'found'
            
        elif mid_num > target:
            return 'left'
        
        elif mid_num < target:
            return 'right'   
    
    return binary_search(0,len(nums)-1,condition)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return (start_position(nums,target),end_position(nums,target))
        
