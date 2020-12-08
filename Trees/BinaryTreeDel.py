# BINARY TREE DELETION


class binaryTreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class binaryTree:

    def __init__(self, root=None):
        self.root = root

    def _insertNode(self, node, value):

        if value < node.value:
            if node.left is None:
                node.left = binaryTreeNode(value)
            else:
                self._insertNode(node.left, value)

        elif value > node.value:
            if node.right is None:
                node.right = binaryTreeNode(value)
            else:
                self._insertNode(node.right, value)

    def insertNode(self, value):

        if(self.root is None):
            self.root = binaryTreeNode(value)

        else:
            self._insertNode(self.root, value)

    def _printInorderTraversal(self, currentNode):
        if(currentNode is None):
            return []

        return self._printInorderTraversal(currentNode.left) + [currentNode.value] + self._printInorderTraversal(currentNode.right)

    def printTree(self):

        if(self.root is None):
            return 'Empty Tree'

        return self._printInorderTraversal(self.root)

    # def deletion


if __name__ == "__main__":

    nodeInstance = binaryTree()

    nodeInstance.insertNode('9')
    nodeInstance.insertNode('7')
    nodeInstance.insertNode('8')
    nodeInstance.insertNode('2')
    nodeInstance.insertNode('11')

    print(nodeInstance.printTree())
