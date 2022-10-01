# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_str = ''
        itr = head
        i=0
        while itr:
            binary_str += str(itr.val)
            itr = itr.next
            i += 1
        decimal = int(binary_str, 2)
        return decimal
