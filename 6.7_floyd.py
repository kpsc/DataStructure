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


class Floyd:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()
        self.nodes = list(self.G.nodes)
        self.number_of_nodes = self.G.number_of_nodes
        self.edges = sorted(graph, key=lambda x: x[2])

        print('networkx: ', nx.floyd_warshall(self.G))
        self.floyd()
        self.draw()

    def createGraph(self):
        G = nx.Graph()
        G.add_weighted_edges_from(graph)

        return G

    def found_path(self, distances, paths, source='v0', target='v8'):
        distance = distances[source][target]
        path = [source]

        tmp = source
        while paths[tmp][target] != target:
            tmp = paths[tmp][target]
            path.append(tmp)
        path.append(target)

        return f'{source}-{target} {distance}: {path}'

    def found_all(self, distances, paths):
        print('floyd:')
        for u in self.nodes:
            for v in self.nodes:
                if u != v:
                    print(self.found_path(distances, paths, u, v))

    def floyd(self):
        paths = {u: {v: v for v in self.nodes} for u in self.nodes}
        distances = {u: {v: np.inf for v in self.nodes} for u in self.nodes}

        # init
        for u in self.nodes:
            for v in self.nodes:
                if v == u:
                    distances[u][v] = 0
                elif v in self.G[u]:
                    distances[u][v] = self.G[u][v]['weight']
        
        for k in self.nodes:    # 通过使用中间节点，来求得所有节点之间的最短距离
            for u in self.nodes:
                for v in self.nodes:
                    if distances[u][v] > distances[u][k] + distances[k][v]:
                        distances[u][v] = distances[u][k] + distances[k][v]
                        paths[u][v] = paths[u][k]

        self.found_all(distances, paths)
          
    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    Floyd()        
