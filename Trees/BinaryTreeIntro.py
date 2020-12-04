# BINARY TREE INTRODUCTION


class binaryTreeNode:

    def __init__(self, value, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right


if __name__ == "__main__":

    node1 = binaryTreeNode('1')
    node2 = binaryTreeNode('2')
    node3 = binaryTreeNode('3')

    node1.left = node2
    node1.right = node3
