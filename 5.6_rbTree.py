import random
from utils import PLRbTree

class TreeNode:
    def __init__(self, val, color='R'):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = color

    @property
    def isblack(self):
        return self.color == 'B'
    
    @property
    def isred(self):
        return self.color == 'R'

    def setblack(self):
        self.color = 'B'

    def setred(self):
        self.color = 'R'


# 性质1. 节点是红色或黑色
# 性质2. 根节点是黑色
# 性质3. 每个叶节点（空节点或nil）均是黑色的
# 性质4. 每个红色节点的两个子节点均为黑色 （路径上不能有两个连续的红色节点）
# 性质5. 从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点
class RBTree:
    def __init__(self, val_list=[]):
        self.root = None
        if isinstance(val_list, int):
            val_list = [val_list]

        for n in val_list:
            self.insert(n)

    def _rRotate(self, y):
        #################################################
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

    def _lRotate(self, y):
        ##############################################
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

    def _reColorInsert(self, node):
        # 对插入过程的颜色进行处理
        # 检查节点及父节点是否破坏了性质
        # 性质2. 根节点是黑色
        # 性质4. 每个红色节点的两个子节点均为黑色
        if self.root == node or self.root == node.parent:
            self.root.setblack()
            return

        if node.parent.isblack:
            return

        grand = node.parent.parent
        if not grand:  # 没有祖父节点，近似于在根节点直接插入，但根节点可能会在前面的处理中被处理成红色，故需要递归身上再进行检查
            self._reColorInsert(node.parent)
            return
        
        # 父节点及叔叔节点均为红色
        if (grand.left and grand.left.isred) and (grand.right and grand.right.isred):
            grand.left.setblack()
            grand.right.setblack()
            grand.setred()
            self._reColorInsert(grand)
            return

        # 父节点为红色，叔叔为黑色，插入节点、父节点及祖父节点为左倾或右倾
        parent = node.parent
        if parent.left == node and grand.left == parent:
            parent.setblack()
            grand.setred()
            self._rRotate(grand)
            return
        if parent.right == node and grand.right == parent:
            parent.setblack()
            grand.setred()
            self._lRotate(grand)
            return

        if parent.left == node and grand.right == parent:
            self._rRotate(parent)
            self._reColorInsert(parent)
            return
        if parent.right == node and grand.left == parent:
            self._lRotate(parent)
            self._reColorInsert(parent)

    def insert(self, data):
        if self.root == None:
            self.root = TreeNode(data)
            self.root.setblack()
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
            new_node.parent = parent
            if data < parent.val:
                parent.left = new_node
            else:
                parent.right = new_node
            self._reColorInsert(new_node)
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
            print(f'not found {data} in RBTree')
            return False

        node = self._delReplace(node)
        self._reColorDelete(node)
        self._delPost(node)

        return True

    def _preNode(self, node):
        if not node.left:
            return None
        pre_node = node.left
        while pre_node.right:
            pre_node = pre_node.right
        return pre_node

    def _postNode(self, node):
        if not node.right:
            return None
        post_node = node.right
        while post_node.left:
            post_node = post_node.left
        return post_node

    def _delReplace(self, node):
        post_node = self._postNode(node)
        if post_node:
            node.val, post_node.val = post_node.val, node.val
            return self._delReplace(post_node)

        pre_node = self._preNode(node)
        if pre_node:
            node.val, pre_node.val = pre_node.val, node.val
            return self._delReplace(pre_node)
        # 被替换节点没有子节点时进行删除操作
        return node

    def _delPost(self, node):
        if self.root == node:
            self.root = None
        elif node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
        node.parent = None

    def _reColorDelete(self, node):
        # 删除节点为根节点或红色节点，直接删除
        if self.root == node or node.isred:
            return

        # 删除节点为黑色
        is_left = node.parent.left == node
        brother = node.parent.right if is_left else node.parent.left
        # 兄弟节点为红色
        if brother and brother.isred:
            node.parent.setred()
            brother.setblack()
            if is_left:
                self._lRotate(node.parent)
            else:
                self._rRotate(node.parent)
            return

        # 兄弟为黑色，且兄弟节点没有子节点或全为黑色子节点
        all_none = brother and  not brother.left and not brother.right
        all_black = brother and (brother.left and brother.left.isblack) and (brother.right and brother.right.isblack)
        if all_none or all_black:
            brother.setred()
            if node.parent.isred:
                node.parent.setblack()
                return
            self._reColorDelete(node.parent)

        # 兄弟为黑色，兄弟节点的同侧子节点为红色
        brother_same_side_red_left = brother and not is_left and brother.left and brother.left.isred
        brother_same_side_red_right = brother and is_left and brother.right and brother.right.isred
        if brother_same_side_red_left or brother_same_side_red_right:
            if node.parent.isred:
                brother.setred()
            else:
                brother.setblack()
            node.parent.setblack()

            if brother_same_side_red_right:
                brother.right.setblack()
                self._lRotate(node.parent)
            else:
                brother.left.setblack()
                self._rRotate(node.parent)
            return

        # 兄弟为黑色，兄弟异侧子节点为红色，兄弟同侧子节点为黑色或无节点
        brother_diff_side_red_left = brother and is_left and brother.left and brother.left.isred
        brother_diff_side_red_right = brother and not is_left and brother.right and brother.right.isred
        if brother_diff_side_red_left or brother_diff_side_red_right:
            brother.setred()
            if brother_diff_side_red_left:
                brother.left.setblack()
                self._rRotate(brother)
            else:
                brother.right.setblack()
                self._lRotate(brother)
            self._reColorDelete(node)


if __name__ == '__main__':

    tree = RBTree()
    data = list(range(1, 20))
    # random.shuffle(data)
    # print(data)
    for i in [2, 8, 9, 11, 13, 17, 14, 18, 15, 4, 5, 1, 3, 6, 12, 7, 16, 19, 10]:
        tree.insert(i)
        # show_rb_tree(tree.root)

    # random.shuffle(data)
    # print(data)
    for i in [4, 14, 15, 19, 1, 16, 12, 10, 9, 6, 17, 2, 3, 8, 7, 18, 11, 5, 13]:
        print("delete ", i)
        tree.delete(i)
        PLRbTree(tree)
