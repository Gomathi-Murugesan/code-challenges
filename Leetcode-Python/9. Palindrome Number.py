class Solution:
    def isPalindrome(self, x: int) -> bool:
        start = 0
        #print(reversed(x))
        str_x = str(x)
        for i in range(len(str_x)-1,-1,-1):
            if str_x[i] != str_x[start]:
                return False
            start += 1
        return True