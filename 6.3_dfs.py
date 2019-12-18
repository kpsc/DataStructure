import networkx as nx
import matplotlib.pyplot as plt


graph = [('A', 'B'), ('A', 'F'), 
         ('B', 'C'), ('B', 'I'), ('B', 'G'), 
         ('C', 'D'), ('C', 'I'), 
         ('D', 'E'), ('D', 'H'), ('D', 'G'), ('D', 'I'), 
         ('E', 'F'), ('E', 'H'), 
         ('F', 'A'), ('F', 'G'), 
         ('G', 'B'), ('G', 'D'), ('G', 'H'), 
         ('H', 'D'), ('H', 'E')]


class DFS:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()
        self.visited = set()

        print('networkx: ', list(nx.dfs_tree(self.G, 'A')))
        print('dfs_tree: ', self.dfs_tree('A'))
        self.draw()

    def createGraph(self):
        G = nx.Graph()
        G.add_edges_from(graph)

        return G

    def dfs_tree(self, u):
        nodes = [u]
        self.visited.add(u)
        
        for v in self.G[u]:
            if v not in self.visited:
                nodes.extend(self.dfs_tree(v))

        return nodes

    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    DFS()
