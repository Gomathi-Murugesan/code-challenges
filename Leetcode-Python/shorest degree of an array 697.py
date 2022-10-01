class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) == None:
                d[nums[i]] = [i]
            elif d[nums[i]]:
                d[nums[i]].append(i)
        degree = 0
        shortest_path = 0
        for i in nums:
            length = len(d[i])
            if length > degree:
                degree = length
                #if length == 1:
                 #   shortest_path = 1
                #else:
                start = d[i][0]
                end = d[i][length-1]
                shortest_path = (end-start) + 1
            elif length == degree:
                start = d[i][0]
                end = d[i][length-1]
                if ((end-start) + 1) < shortest_path:
                    shortest_path = (end-start) + 1
        return shortest_path
            
