# shortest_paths 最短路径

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#####################
#        v3         #
#       / | \       #
#     v1  |  v6     #
#    /  \ | /  \    #
#   v0   v4     v8  #
#    \  / | \  /    #
#     v2  |  v7     #
#       \ | /       #
#        v5         #
#####################

graph = [('v0', 'v1', 1), ('v0', 'v2', 5), 
         ('v1', 'v2', 3), ('v1', 'v3', 7), ('v1', 'v4', 5), 
         ('v2', 'v4', 1), ('v2', 'v5', 7), 
         ('v3', 'v4', 2), ('v3', 'v6', 3), 
         ('v4', 'v5', 3), ('v4', 'v6', 6),  ('v4', 'v7', 9), 
         ('v5', 'v7', 5),  
         ('v6', 'v7', 2), ('v6', 'v8', 7), 
         ('v7', 'v8', 4)]


class Dijkstra:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()
        self.nodes = list(self.G.nodes)
        self.edges = sorted(graph, key=lambda x: x[2])

        print('networkx: ', nx.single_source_dijkstra(self.G, 'v0', 'v8', weight='weight'))
        print('dijkstra: ', self.dijkstra('v0', 'v8'))
        self.draw()

    def createGraph(self):
        G = nx.Graph()
        G.add_weighted_edges_from(graph)

        return G

    def found_path(self, parent, source, target):
        path = [target]
        preview = parent[target]
        while preview != source:
            path.insert(0, preview)
            preview = parent[preview]
        path.insert(0, source)

        return path

    def dijkstra(self, source, target):
        parent = {n: n for n in self.nodes}          # 记录最短路径中的前驱节点
        distance = {n: np.inf for n in self.nodes}   # 记录最短路径中的距离

        visited = set()           # 用于记录已经计算出最短路径的节点
        visited.add(source)
        
        distance[source] = 0      # 初始时，只有source节点，明确最短路径
        for node in self.G[source]:
            parent[node] = source
            distance[node] = self.G[source][node]['weight']

        for node in self.nodes:
            if node == source:
                continue

            min_ = np.inf        # 根据路径数组，求出当前路径中的最近节点
            k = node
            for next_ in self.nodes:
                if next_ in visited:
                    continue
                if distance[next_] < min_:
                    min_ = distance[next_]
                    k = next_
            visited.add(k)

            for n in self.nodes:
                if n in visited:
                    continue
                if n in self.G[k] and min_ + self.G[k][n]['weight'] < distance[n]:   # 根据最近节点，对距离进行更新
                    distance[n] = min_ + self.G[k][n]['weight']
                    parent[n] = k

        return distance[target], self.found_path(parent, source, target)
          
    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    Dijkstra()        
