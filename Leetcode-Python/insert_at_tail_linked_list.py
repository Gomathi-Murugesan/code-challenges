def insertNodeAtTail(head, data):
    newNode = SinglyLinkedListNode(data)
    
    temp = head
    
    if head == None:
        return newNode
    
    else:
        while temp != None:
            if temp.next == None:
                break
            temp = temp.next
        
        temp.next = newNode
        return head


def insertNodeAtTail(head, data):
    
    itr = head
    if head is None:
        node = SinglyLinkedListNode(data)
        head = node
        return node
    else:
        while itr.next:
            itr = itr.next
        node = SinglyLinkedListNode(data)
        itr.next = node
        return head
