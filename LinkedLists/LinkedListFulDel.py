# DELETING LINKEDLIST FULLY

class linkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtBeginning(self, value):
        node = linkedListNode(value)
        if(self.head is None):
            self.head = node
            return
        node.nextNode = self.head
        self.head = node

    def printList(self):
        currentNode = self.head
        if(self.head is None):
            print("List is empty")
            return

        while (currentNode is not None):
            print(currentNode.value, '->', end="")
            currentNode = currentNode.nextNode
        print('None')

    def delFulList(self):
        if(self.head is None):
            print("Nothing to delete")
            return

        currentNode = self.head
        while (currentNode is not None):
            temp = currentNode
            del temp
            currentNode = currentNode.nextNode
            self.head = currentNode


if __name__ == "__main__":
    node = linkedList()
    node.insertAtBeginning("4")
    node.insertAtBeginning("5")
    node.insertAtBeginning("6")
    node.printList()
    node.delFulList()
    node.printList()
