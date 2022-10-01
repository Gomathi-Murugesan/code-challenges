class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_list = sorted(intervals, key=lambda x:x[0])
        #print(sorted_list)
        i = 0
        while i < len(sorted_list)-1:
            #print('len', len(sorted_list)-1)
            #print('i', i)
            if sorted_list[i][1] >= sorted_list[i+1][0]:
                if sorted_list[i][1] > sorted_list[i+1][1]:
                    new_pair = [sorted_list[i][0], sorted_list[i][1]]
                else:
                    new_pair = [sorted_list[i][0], sorted_list[i+1][1]]
                sorted_list[i] = new_pair
                sorted_list = sorted_list[:i+1] + sorted_list[i+2:]
                i = i
                #sorted_list.remove(i+1)
                #print(sorted_list)
            else:
                i = i + 1
        
        return(sorted_list)
                
