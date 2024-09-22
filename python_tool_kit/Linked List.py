class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


def get_k_node(head: Node, index: int):
    assert head is not None, "Head is None - need to be Node"
    current = head  # Initialise temp
    count = 0  # Index of current node

    # Loop while end of linked list is not reached
    while current:
        if count == index:
            return current
        count += 1
        current = current.next
    # if we get to this line, the caller was asking
    # for a non-existent element so we assert fail
    assert False, "index out of range"
    return 0


def get_element_index(head: Node, element: int):
    current = head  # Initialise temp
    index = 0  # Index of current node

    # Loop while end of linked list is not reached
    while current:
        if current.data == element:
            return index
        index += 1
        current = current.next
    return -1  # not found


def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


# Driver code
head = Node(10)
head.next = Node(12)
head.next.next = Node(11)
head.next.next.next = Node(14)
head.next.next.next.next = Node(17)
head.next.next.next.next.next = Node(120)
head.next.next.next.next.next.next = Node(1110)

printList(head)
print(get_k_node(head, 2).data)  # 11
print(get_element_index(head, 11))  # 2
# print(get_k_node(None, 11))  #
print(get_element_index(None, 11))  # 2
