# Minimum Cost Spanning Tree   最小生成树
# 一个连通图的生成树是一个极小的连通子图，它含有图中全部的奇点，但只有足以构成一棵树的 n-1 条边
# kruskal: 通过对边进行排序，每次选择权值最小的边的两个节点加入到最小生成树中，且不能构成环，直到所有节点加入到最小生成树中

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


class Kruskal:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()
        self.nodes = list(self.G.nodes)
        self.edges = sorted(graph, key=lambda x: x[2])

        print('networkx: ', nx.minimum_spanning_tree(self.G, algorithm='kruskal').edges(data=True))
        print('kruskal: ', self.kruskal())
        self.draw()

    def createGraph(self):
        G = nx.Graph()
        G.add_weighted_edges_from(graph)

        return G

    def find(self, parent, n):
        while parent[n] != n:   # 若不一致，说明已经加入到最小生成树中
            n = parent[n]

        return parent[n]

    def kruskal(self):
        mst = []

        parent = {n:n for n in self.nodes}   # 记录与当前节点相连的节点
        for i in range(len(self.edges)):
            n = self.find(parent, self.edges[i][0])
            m = self.find(parent, self.edges[i][1])
            if n != m:
                parent[n] = m
                mst.append(self.edges[i])

        return mst
          
    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    Kruskal()        
