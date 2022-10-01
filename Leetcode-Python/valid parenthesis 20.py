from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        brace={'(':')', '{':'}', '[':']' }
        stack = deque()
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        for i in s:
            if i in brace.keys():
                stack.append(i)
            elif i in brace.values():
                if len(stack) >= 1:
                    stack_out = stack.pop() 
                    if brace[stack_out] != i:
                        return False
                    elif brace[stack_out] == stack_out:
                        continue
                else:
                    return False
        if len(stack) == 0:
            return True
