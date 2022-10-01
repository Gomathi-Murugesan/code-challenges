## code to find the number of rotations or the position or index of the first value... 
## in unique elements in the list

def find_number_rotation(nums):
    
    def condition(mid):
        mid_number = nums[mid]
    
        if mid > 0 and mid_number < nums[mid-1] :
            return 'found'
        
        elif mid > 0 and mid_number < nums[len(nums)-1]:
            return 'left'  
        
        else:
            return 'right'
        
    return binary_search(0,len(nums)-1,condition)

## function to search the target number    
def find_target(nums,target):
    
    def condition(mid):
        mid_num = nums[mid]
        
        if mid_num == target:
            return 'found'
        
        elif mid_num > target:
            return 'left'
        
        else:
            return 'right'
    
    return binary_search(0,len(nums)-1,condition)   
    
 ## binary search algorithm
    
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


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            output = -1
        else:    
            pivot = find_number_rotation(nums)
            
    
            if pivot == -1: ## no rotation... so searching directly using the binary search 
                output = find_target(nums, target) 
        
            else:
                output = find_target(nums[0:pivot], target) ## check the first half of the list for the target 
                if output == -1: ## target is not in the first part
                    output = find_target(nums[pivot:],target) ## check the second part for the target
                    if output != -1: ## if target is present add the target position with size of the first half
                        output = pivot + output
        return output
            
 
