# Delete the middle node of a linked list and print the resulting linked list.

# Input Description

# First line represents the size of the linked list.
# Next line represents the sequence of numbers as the node value of the linked list.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToList(self, data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def __str__(self):
        linkedListStr = ""
        temp = self.head

        while temp:
            linkedListStr = linkedListStr + str(temp.data) + "->"
            temp = temp.next
        return linkedListStr + "NULL"

    def deleteMid(self):

        if(self.head is None or self.head.next is None):
            return
        slow_Ptr = self.head
        fast_Ptr = self.head

        prev = None

        while (fast_Ptr is not None and fast_Ptr.next is not None):
            fast_Ptr = fast_Ptr.next.next
            prev = slow_Ptr
            slow_Ptr = slow_Ptr.next
        prev.next = slow_Ptr.next


linkedList = LinkedList()

linkedList.addToList(1)
linkedList.addToList(2)
linkedList.addToList(3)
linkedList.addToList(4)
# linkedList.addToList(5)


print(linkedList)

linkedList.deleteMid()

print(linkedList)
