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


class BFS:
    def __init__(self, G=None):
        self.G = G if G else self.createGraph()

        print('networkx: ', list(nx.bfs_tree(self.G, 'A')))
        print('bfs_tree: ', self.bfs_tree('A'))
        self.draw()

    def createGraph(self):
        G = nx.Graph()
        G.add_edges_from(graph)

        return G

    def bfs_tree(self, u):
        nodes = []
        visited = set()

        curQueue = [u]
        while len(curQueue) > 0:
            n = curQueue.pop(0)
            nodes.append(n)
            visited.add(n)

            for v in self.G[n]:
                if v not in visited and v not in curQueue:
                    curQueue.append(v)
        
        return nodes

    def draw(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    BFS()        
