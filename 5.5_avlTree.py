from utils import PLTtree


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.bf = 0


class AVLTree:
    def __init__(self, val_list=[]):
        self.root = None
        if isinstance(val_list, int):
            val_list = [val_list]

        for n in val_list:
            self.insert(n)

    def height(self, node):
        return node.height if node else 0

    def _llRotate(self, y):
        #################################################
        # x/y节点: 左子树高度大于右子树                   #
        # y/x 高度调整，递归对 y 及其父节点调整即可        #
        # LL T1<Z<T2< X <T3<Y<T4                        #
        #        y                              x       #
        #       / \                           /   \     #
        #      x   T4     向右旋转 (y)        z     y    #
        #     / \       - - - - - - - ->    / \   / \   #
        #    z   T3                        T1 T2 T3 T4  #
        #   / \                                         #
        # T1   T2                                       #
        #################################################
        x = y.left
        parent = y.parent
        t3 = x.right
        if parent != None:
            if y == parent.left:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x
        y.parent = x
        x.parent = parent
        y.left = t3
        x.right = y
        if t3 != None:
            t3.parent = y

    def _rrRotate(self, y):
        ##############################################
        # y/x: 右子树高度大于左子树                    #
        # y/x 高度调整，递归对 y 及其父节点调整即可     #
        # RR T1<Y<T2< X <T3<Z<T4                     #
        #    y                             x         #
        #  /  \                          /   \       #
        # T1   x      向左旋转 (y)       y     z      #
        #     / \   - - - - - - - ->   / \   / \     #
        #    T2  z                    T1 T2 T3 T4    #
        #       / \                                  #
        #      T3 T4                                 #
        ##############################################
        x = y.right
        parent = y.parent
        t2 = x.left
        if parent != None:
            if y == parent.left:
                parent.left = x
            else:
                parent.right = x
        else:
            self.root = x
        y.parent = x
        x.parent = parent
        y.right = t2
        x.left = y
        if t2 != None:
            t2.parent = y

    def _lrRotate(self, y):
        ########################################################################################
        #  y: 左子树 > 右子树                                                                   #
        #  x: 左子树 < 右子树                                                                   #
        #  y/x/z 高度调整，对 x 及递归对 y 及其父节点调整即可                                     #
        #  LR  T1<X<T2< Z <T3<Y<T4                                                             #
        #         y                                y                              z            #
        #        / \                              / \                           /   \          #
        #       x  t4    向左旋转（x）            z   T4      向右旋转（y）    　x     y         #
        #      / \     --------------->         / \        --------------->   / \   / \        #
        #     T1  z                            x   T3                        T1  T2 T3 T4      #
        #        / \                          / \                                              #
        #       T2  T3                      T1   T2                                            #
        ########################################################################################
        self._rrRotate(y.left)
        self._llRotate(y)

    def _rlRotate(self, y):
        ########################################################################################
        #  y: 左子树 < 右子树                                                                   #
        #  x: 左子树 > 右子树                                                                   #
        #  y/x/z 高度调整，对 x 及递归对 y 及其父节点调整即可                                     #
        # RL: T1<Y<T2< Z <T3<X<T4                                                              #
        #      y                           y                                       z           #
        #     / \                         / \                                    /   \         #
        #    T1  x       向右旋转（x）   　T1  z         向左旋转（y）            y     x        #
        #       / \    - - - - - - ->       / \      - - - - - - - - ->        / \   / \       #
        #      z  T4                       T2  x                              T1 T2 T3 T4      #
        #     / \                             / \                                              #
        #    T2  T3                          T3  T4                                            #
        ########################################################################################
        self._llRotate(y.right)
        self._rrRotate(y)

    def _isbalanced(self, node):
        return abs(self.height(node.left) - self.height(node.right)) <= 1

    def _recompute_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def _rebalanced(self, node):
        while node != None:
            if self._isbalanced(node):
                self._recompute_height(node)
                node = node.parent
            else:
                lheight = self.height(node.left)
                rheight = self.height(node.right)
                if lheight > rheight and self.height(node.left.left) > self.height(node.left.right):
                    self._llRotate(node)
                elif lheight < rheight and self.height(node.right.left) < self.height(node.right.right):
                    self._rrRotate(node)
                elif lheight > rheight and self.height(node.left.left) < self.height(node.left.right):
                    left = node.left
                    self._lrRotate(node)
                    self._recompute_height(left)
                else:
                    right = node.right
                    self._rlRotate(node)
                    self._recompute_height(right)
                
                while node:
                    self._recompute_height(node)
                    node = node.parent

    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
            self.root.height = 1
        else:
            node = self.root
            while node:
                parent = node
                if data == node.val:
                    print(f'{data} has in the Tree')
                    return None
                elif data < node.val:
                    node = node.left
                else:
                    node = node.right

            new_node = TreeNode(data)
            new_node.height = 1
            new_node.parent = parent
            if data < parent.val:
                parent.left = new_node
            else:
                parent.right = new_node

            self._rebalanced(new_node)
        return True
    
    def search(self, data):
        node = self.root
        while node:
            if data < node.val:
                node = node.left
            elif data == node.val:
                return node
            else:
                node = node.right

        return None

    def delete(self, data):
        node = self.search(data)
        if not node:
            print(f'not found {data} in AVLTree')
            return False

        self._del(node)
        return True

    def _del(self, node):
        if node.left == None and node.right == None:
            if node == self.root:
                self.root = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = None
                else:
                    node.parent.right = None
                self._rebalanced(node.parent)
                node.parent = None

        elif node.left == None and node.right != None:
            if node == self.root:
                self.root = node.right
                self.root.parent = None
                node.right = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

                node.right.parent = node.parent
                self._rebalanced(node.parent)
                node.right = None
                node.parent = None

        elif node.left != None and node.right == None:
            if node == self.root:
                self.root = node.left
                self.root.parent = None
                node.left = None
            else:
                if node.val < node.parent.val:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left

                node.left.parent = node.parent
                self._rebalanced(node.parent)
                node.left = None
                node.parent = None

        else:
            min_node = node.right
            while min_node.left:
                min_node = min_node.left

            node.val = min_node.val
            self._del(min_node)
        
    def draw(self, title=''):
        if self.root is None:
            print("An Empty Tree, Nothing to plot")
        else:
            plt_tree = PLTtree(title)
            plt_tree.draw(self.root)


if __name__ == '__main__':
    trees, titles = [], []
    nums = list(range(10))
    bst = AVLTree(nums)
    bst.draw()

    print('insert 1: ', bst.insert(1))
    print('insert 15: ', bst.insert(15))
    bst.draw('insert 15')

    print('insert 20: ', bst.insert(20))
    bst.draw('insert 20')

    print('search 2: ', bst.search(2))
    print('search 25: ', bst.search(25))

    print('delete 7: ', bst.delete(7))
    bst.draw('delete 7')
    print('delete 4: ', bst.delete(4))
    bst.draw('delete 4')
    print('delete 4: ', bst.delete(4))
    bst.draw('delete 4 again')
    print('delete 3: ', bst.delete(3))
    bst.draw('delete 3')
    print('delete 0: ', bst.delete(0))
    bst.draw('delete 0')
