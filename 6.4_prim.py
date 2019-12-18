# Minimum Cost Spanning Tree   最小生成树
# 一个连通图的生成树是一个极小的连通子图，它含有图中全部的奇点，但只有足以构成一棵树的 n-1 条边
# prim: 在剩余的节点集中，找到一条边，与当前的最小生成树连接的权值最小，递归向剩余的子节点中进行

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


graph = [('v0', 'v1', 10), ('v0', 'v5', 11), 
         ('v1', 'v2', 18), ('v1', 'v6', 16), ('v1', 'v8', 12), 
         ('v2', 'v3', 22), ('v2', 'v8', 8), 
         ('v3', 'v4', 20), ('v3', 'v7', 16), ('v3', 'v6', 24), ('v3', 'v8', 21), 
         ('v4', 'v5', 26), ('v4', 'v7', 7), 
         ('v5', 'v6', 17),  
         ('v6', 'v7', 19)]


class Prim:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()
        self.nodes = list(self.G.nodes)
        self.num_of_nodes = len(self.nodes)

        print('networkx: ', nx.minimum_spanning_tree(self.G, algorithm='prim').edges(data=True))
        print('prim: ', self.prim())
        self.draw()

    def createGraph(self):
        G = nx.Graph()
        G.add_weighted_edges_from(graph)

        return G

    def prim(self):
        mst = []

        adjvex = [0] * self.num_of_nodes        # 保存相关顶点
        lowcost = [np.inf] * self.num_of_nodes      # 保存其他节点与当前最小生成树之间的距离，当对应值为０时表示相应节点已经在最小生成树中

        adjvex[0], lowcost[0] = 0, 0
        u = self.nodes[0]
        for i, v in enumerate(self.nodes[1:], 1):
            adjvex[i] = 0
            if v in self.G[u]:   # 从节点 u 开始进行计算，将与 u 相连的所有节点加入 lowcost 中，并更新权值
                lowcost[i] = self.G[u][v]['weight']

        for _ in range(1, self.num_of_nodes):
            min_ = np.inf
            
            k = 0   # 查找与当前最小生成树之间距离最近的节点
            for j, w in enumerate(lowcost[1:], 1):
                if w != 0 and w < min_:
                    min_ = w
                    k = j

            u, v = self.nodes[adjvex[k]], self.nodes[k] 
            mst.append((u, v, self.G[u][v]['weight']))

            lowcost[k] = 0    # 节点 k 已进行访问过
            for j in range(1, self.num_of_nodes):     # 与节点 k 相连的节点，根据权值计算是否对lowcost进行更新
                if lowcost[j] != 0 and self.nodes[j] in self.G[self.nodes[k]] and \
                    self.G[self.nodes[k]][self.nodes[j]]['weight'] < lowcost[j]:
                    lowcost[j] = self.G[self.nodes[k]][self.nodes[j]]['weight']
                    adjvex[j] = k
        return mst
          
    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    Prim()        
