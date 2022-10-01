def insertNodeAtHead(llist, data):
    if llist is None:
        node = SinglyLinkedListNode(data)
        llist = node
    else:
        node = SinglyLinkedListNode(data)
        node.next = llist
        llist = node

    return llist
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()
