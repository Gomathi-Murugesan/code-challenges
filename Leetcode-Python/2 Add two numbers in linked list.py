# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = self.get_number(l1)
        number2 = self.get_number(l2)
        sum_numbers = number1 + number2
        #print(sum_numbers)
        #res = list(map(int, str(sum_numbers)))
        #print(res[::-1])
        dict_list=list(str(sum_numbers))
        print(dict_list)
        
        for index, value in enumerate(dict_list):
            if index == 0:
                dict_list[index] = ListNode(val=value, next=None)
            else:
                dict_list[index] = ListNode(val=value, next=dict_list[index-1])     
        
        return dict_list[len(dict_list)-1]
        
                
    def get_number(self,node):
        itr = node
        string = ''
        while itr:
            string = str(itr.val) + string
            itr = itr.next
        integer = int(string)        
        return integer
    

