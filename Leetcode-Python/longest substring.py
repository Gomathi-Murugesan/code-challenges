class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subsets=[]
        #subsets = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                subset = s[i:j]
                temp=[]
                for n in subset:
                    if n not in temp:
                        temp.append(n)
                if len(temp) == len(subset):
                    subsets.append(subset)
        len_subset = 0
        for subset in subsets:
            if len(subset) > len_subset:
                len_subset = len(subset)  
        #print(subsets)
        return len_subset
        
        
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        mx = 0
        st = 0
        for i in range(len(s)):
            while(d[s[i]]):
                d[s[st]] = 0
                st +=1
            d[s[i]] = 1
            mx = max(mx, (i-st)+1)
        return(mx
        
def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        max_len = 0
        start = 0
        end = 0
        for i in range(size):
            print('i',i)
            while s[i] in s[start:end]:
                print('s',s[i])
                print('o',s[start:end])
                start+=1    
            end+=1       
            max_len = max(max_len, (end-start))
        return max_len
