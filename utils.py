import matplotlib.pyplot as plt
import numpy as np


def preorder(tree):
    # 前序遍历
    data = []
    if tree:
        data.append(tree.val)
        data.extend(preorder(tree.left))
        data.extend(preorder(tree.right))
    return data


def lastorder(tree):
    # 后序遍历
    data = []
    if tree:
        data.extend(preorder(tree.left))
        data.extend(preorder(tree.right))
        data.append(tree.val)
    return data
        

def inorder(tree):
    # 中序遍历
    data = []
    if tree:
        data.extend(preorder(tree.left))
        data.append(tree.val)
        data.extend(preorder(tree.right))
    return data


def seqorder(tree):
    # 层序遍历
    data = []
    queue = [tree]

    while len(queue):
        node = queue.pop(0)
        if node:
            queue.extend([node.left, node.right])
            data.append(node.val)
        else:
            data.append(None)

    return data


class PLTtree:
    def __init__(self, title=''):
        self.bbox = dict(boxstyle="circle", fc="white")
        self.arrowprops = dict(arrowstyle = "<|-")

        _, self.ax = plt.subplots()
        self.ax.set_title(title)
        
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
        
    def get_coord(self, coord_prt, depth_le, depth, child_type="left"):
        if child_type == "left":
            x_child = coord_prt[0] - 1 / (2 ** (depth_le + 1))
        elif child_type == "right":
            x_child = coord_prt[0] + 1 / (2 ** (depth_le + 1))
        else:
            raise Exception("No other child type")
        y_child = coord_prt[1] - 1 / depth
        return x_child, y_child
        
    def plot_node(self, node_text, center_point, parent_point):
        self.ax.annotate(node_text, 
                        xy=parent_point,  
                        xytext=center_point, 
                        bbox=self.bbox, 
                        arrowprops=self.arrowprops, 
                        xycoords='axes fraction',
                        textcoords='axes fraction',
                        va="bottom", 
                        ha="center")
                
    def draw(self, root):
        depth = self.height(root)
        coord0 = (1/2, 1 - 1/(2*depth))
        node_queue = list()
        coord_queue = list()
        self.plot_node(str(root.val), coord0, coord0)
        node_queue.append(root)
        coord_queue.append(coord0)
        cur_level = 0
        while len(node_queue):
            q_len = len(node_queue)
            while q_len:
                q_node = node_queue.pop(0)
                coord_prt = coord_queue.pop(0)
                q_len = q_len - 1
                if q_node.left is not None:
                    xc, yc = self.get_coord(coord_prt, cur_level + 1, depth, "left")
                    element = str(q_node.left.val)
                    self.plot_node(element, (xc, yc), coord_prt)
                    node_queue.append(q_node.left)
                    coord_queue.append((xc, yc))
                if q_node.right is not None:
                    xc, yc = self.get_coord(coord_prt, cur_level + 1, depth, "right")
                    element = str(q_node.right.val)
                    self.plot_node(element, (xc, yc), coord_prt)
                    node_queue.append(q_node.right)
                    coord_queue.append((xc, yc))
            cur_level += 1
        plt.show()
        

class PLRbTree:
    def __init__(self, tree):
        if tree.root is None:
            print("An Empty Tree, Nothing to plot")
        self.show_rb_tree(tree.root)

    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_node_count(self, node):
        if not node:
            return 0
        return 1 + self.get_node_count(node.left) + self.get_node_count(node.right)

    def show_node(self, node, ax, height, index, font_size=16):
        if not node:
            return
        x1, y1 = None, None
        if node.left:
            x1, y1, index = self.show_node(node.left, ax, height-1, index, font_size)
        x = 100 * index - 50
        y = 100 * height - 50
        if x1:
            plt.plot((x1, x), (y1, y), linewidth=2.0,color='b')
        circle_color = "black" if node.isblack else 'r'
        text_color = "beige" if node.isblack else 'black'
        ax.add_artist(plt.Circle((x, y), 50, color=circle_color))
        ax.add_artist(plt.Text(x, y, node.val, color= text_color, fontsize=font_size, horizontalalignment="center",verticalalignment="center"))

        index += 1
        if node.right:
            x1, y1, index = self.show_node(node.right, ax, height-1, index, font_size)
            plt.plot((x1, x), (y1, y), linewidth=2.0, color='b')

        return x, y, index

    def show_rb_tree(self, tree, title=''):
        _, ax = plt.subplots()
        height =  self.get_height(tree)
        plt.ylim(0, height*100+100)
        plt.xlim(0, 100 * self.get_node_count(tree) + 100)
        self.show_node(tree, ax, height, 1)
        plt.show()

