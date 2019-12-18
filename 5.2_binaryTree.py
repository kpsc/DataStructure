from utils import preorder, inorder, lastorder, seqorder


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insertLeft(self, data):
        if isinstance(data, BinaryTree):
            newNode = data
        else:
            newNode = BinaryTree(data)

        if self.left == None:
            self.left = newNode
        else:
            t = newNode
            t.left = self.left
            self.left = t

    def insertRight(self, data):
        if isinstance(data, BinaryTree):
            newNode = data
        else:
            newNode = BinaryTree(data)

        if self.right == None:
            self.right = newNode
        else:
            t = newNode
            t.right = self.right
            self.right = t


if __name__ == '__main__':
    tree = BinaryTree('a')

    trl = BinaryTree('b')
    trl.insertLeft('d')
    trl.insertRight('e')

    trr = BinaryTree('c')
    trr.insertLeft('f')
    trr.insertRight('g')

    tree.insertLeft(trl)
    tree.insertRight(trr)

    print('前序：', preorder(tree))
    print('中序：', inorder(tree))
    print('后序：', lastorder(tree))
    print('层序：', seqorder(tree))

