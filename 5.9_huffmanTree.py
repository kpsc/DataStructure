from utils import PLTtree

# 哈夫曼树是一种权重编码的树，将较大权重节点靠近树根，小权重的节点远离树根
# 所有信息存在叶子节点中，根据左右子树将信息转换成0/1编码
# 由底向上构建哈夫曼树
#       50
#     /    \
#    /      \
#   21      29
#  /   \      / \
# 9-a 12-b  14  15-f
#          /  \
#         6-c  8
#            / \
#          3-d  5-e


class TreeNode:
    def __init__(self, key, val, isleaf=True):
        self.key = key
        self.val = val  # weight
        self.left = None
        self.right = None
        self.isleaf = isleaf


class Huffman:
    def __init__(self, data):
        self.node = [TreeNode(d[0], d[1]) for d in data]
        self.root = None
        self._build()
        self.code()
        self.draw()

    def _build(self):
        while len(self.node) > 1:
            self.node.sort(key=lambda x: x.val)
            newNode = TreeNode(None, self.node[0].val + self.node[1].val, isleaf=False)
            newNode.left = self.node.pop(0)
            newNode.right = self.node[0]
            self.node[0] = newNode
        self.root = self.node[0]

    def preorder(self, tree, code):
        if not tree:
            return code
        elif tree.isleaf:
            print(f'{tree.key}: {str(code)[1:-1]}')
            code.pop(-1)
            return code
        code.append(0)
        code = self.preorder(tree.left, code)

        code.append(1)
        code = self.preorder(tree.right, code)
        if code and len(code) > 0:   # 遍历完右子树后要额外向上回退
            code.pop(-1)
        return code if code else []
        
    def code(self):
        self.preorder(self.root, [])
    
    def draw(self, title=''):
        if self.root is None:
            print("An Empty Tree, Nothing to plot")
        else:
            plt_tree = PLTtree(title)
            plt_tree.draw(self.root)


if __name__ == '__main__':
    data = [('a', 9), ('b', 12), ('c', 6), ('d', 3), ('e', 5), ('f', 15)]

    huffman = Huffman(data)
