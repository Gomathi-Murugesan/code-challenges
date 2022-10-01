def compare_lists(llist1, llist2):
    def calculate_string(list1):
        str1 = ''
        itr1 = list1
        while itr1:
            str1 += str(itr1.data)
            itr1=itr1.next
        return str1
    
    list_str1 = calculate_string(llist1)
    list_str2 = calculate_string(llist2)
    
    if list_str1 == list_str2:
        return 1
    else:
        return 0    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()

