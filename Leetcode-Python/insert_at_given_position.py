def insertNodeAtPosition(llist, data, position):
    if position == 0:
        node = SinglyLinkedListNode(data)
        llist = node
        return llist
    
    count = 0
    itr = llist
    while count < position-1:
        itr = itr.next
        count += 1
    node = SinglyLinkedListNode(data)
    node.next = itr.next
    itr.next = node
    
    return llist    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()

