import networkx as nx
import matplotlib.pyplot as plt
#          A
#        /    \
#       /       \    
#     B-----G-----F
#    / \    | \    \   
#   /   \   |   H   \  
#  /     I  |  /  \  \
# /       \ | /    \  |
# C -------- D -------E



# G = nx.Graph()
# G.add_node(node_for_adding, **attr)     # G.add_node(1, time='5pm')
# G.add_nodes_from([1, 2, 3])
# G.add_edge(u_of_edge, v_of_edge, **attr)
# G.add_edges_from([(1, 2), (3, 4)])
# G.add_weighted_edges_from

# G.remove_node(n)
# G.remove_nodes_from(nodes)
# G.remove_edge(u, v)
# G.remove_edges_from(ebunch)

# G.clear()
# G.number_of_nodes()
# G.number_of_edges()
# G.number_of_selfloops()
# G.nodes, G.edges, G.adj[1]/G.neighbors(1), G.degree[1]

# nx.bfs_tree(G, source, reverse=False, depth_limit=None)
# nx.dfs_tree(G, source=None, depth_limit=None)
# nx.dijkstra_path(G, source, target, weight='weight')
# nx.floyd_warshall(G, weight='weight')
# minimum_spanning_tree(G, weight='weight', algorithm='kruskal', ignore_nan=False)   kruskal / prim

# Minimum Cost Spanning Tree   最小生成树
# 一个连通图的生成树是一个极小的连通子图，它含有图中全部的奇点，但只有足以构成一棵树的 n-1 条边
# prim: 在剩余的节点集中，找到一条边，与当前的最小生成树连接的权值最小，递归向剩余的子节点中进行
# kruskal：根据边来构造最小生成树，每次加入权值最小的一个边

# shortest_paths 最短路径

def test():
    G = nx.Graph()
    G.add_edge('a', 'b', weight=4)
    G.add_edge('b', 'd', weight=2)
    G.add_edge('a', 'c', weight=3)
    G.add_edge('c', 'd', weight=4)
    p = nx.shortest_path(G, 'a', 'd', weight='weight')
    nx.draw(G, with_labels=True)
    plt.show()
    print(p)


if __name__ == '__main__':
    test()
