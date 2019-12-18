# 有向图中的遍历，若在图中有 a->b 的一条边，则遍历序列中a必定要在b的前面
# 拓扑排序是节点的非唯一排列，从u到v的边意味着u以拓扑排序顺序出现在v之前

# shortest_paths 最短路径

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
graph = [('v0', 'v4'), ('v0', 'v5'), ('v0', 'v11'),
         ('v1', 'v2'), ('v1', 'v4'), ('v1', 'v8'),
         ('v2', 'v5'), ('v2', 'v6'), ('v2', 'v9'),
         ('v3', 'v2'), ('v3', 'v13'), 
         ('v4', 'v7'), 
         ('v5', 'v8'), ('v5', 'v12'), 
         ('v6', 'v5'), 
         ('v8', 'v7'), 
         ('v9', 'v10'), ('v9', 'v11'), 
         ('v10', 'v13'), 
         ('v12', 'v9')]


class Topologic:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()
        self.nodes = list(self.G.nodes)
        self.number_of_nodes = self.G.number_of_nodes()

        print('networkx: ', list(nx.topological_sort(self.G)))
        print('topologic: ', self.topologic())
        self.draw()

    def createGraph(self):
        G = nx.DiGraph()
        G.add_edges_from(graph)

        return G

    # https://www.cnblogs.com/zhaojieyu/p/8543136.html
    def topologic(self):
        in_degrees = dict((u,0) for u in self.nodes)   #初始化所有顶点入度为0
        for u in self.nodes:
            for v in self.G[u]:
                in_degrees[v] += 1       #计算每个顶点的入度
        nodes_0 = [u for u in in_degrees if in_degrees[u] == 0]   # 筛选入度为0的顶点

        sequence = []
        while nodes_0:
            u = nodes_0.pop()  # 选择方式不同，序列结果也不一样，但都满足要求
            sequence.append(u)
            for v in self.G[u]:
                in_degrees[v] -= 1       #移除其所有指向
                if in_degrees[v] == 0:
                    nodes_0.append(v)          #再次筛选入度为0的顶点
        if len(sequence) == self.number_of_nodes:       #如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
            return sequence
        else:
            print("there's a circle.")
            return None
          
    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    Topologic()        
