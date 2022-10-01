class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        d={}
        for i in range(len(nums)):
            if d.get(nums[i]) == None:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        
        for first_num in nums:
            second_num = target - first_num
            if d.get(second_num) != None:
                if second_num == first_num and len(d[first_num]) > 1:
                    return(d[first_num][0],d[first_num][1])
                if second_num != first_num and len(d[first_num]) == 1:
                    return(d[first_num][0],d[second_num][0])
