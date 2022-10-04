class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        len_str = len(first_str)
        output_str = ""
        if len_str == 0:
            return output_str
        if len(strs) == 1:
            return first_str
        for i in range(0,len_str,1):
            print('f',first_str[i])
            for j in range(1,len(strs),1):
                next_str = strs[j]
                if i<len(next_str) and (first_str[i] == next_str[i]):
                    print('loop',first_str[i])
                    continue
                else:
                    return output_str
            output_str += first_str[i]
            print('o',output_str)
        
        return output_str