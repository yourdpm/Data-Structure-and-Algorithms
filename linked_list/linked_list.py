class Node:

    def __init__(self, data):
        self.data = data
        self.next = None # Initialize next as null

class LinkedList:

    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp:
            print(" %d" % (temp.data))
            temp = temp.next

    def push(self, new_data):
        """ Add a node at the front"""
        new_node = Node(new_data)

        new_node.next = head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        """Add a node after a given node"""
        if prev_node is None:
            print('The given previous node must in Linked List.')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        """Add a node at the end"""
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNodeByKey(self, key):
        """
        Given a reference to the head of a list and a ket
        delete the first occurrence of key in linked list
        """
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def deleteNodeByPosition(self, position):
        if self.head == None:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    def getCount(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next
        return count

    def search(self, x):
        """
        Check whether the value x present in the linked list
        """
        current = self.head

        while current is not None:
            if current.data == x:
                return True

            current = current.next
        
        return False

    def getNthNode(self, head, position, llist):
        count = 0
        if head:
            if count == position:
                print(head.data)
            else:
                llist.getNthNode(head.next, position - 1, llist)
        else:
            print('Index Doesn\'t exist')