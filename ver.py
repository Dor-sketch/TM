import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add edges to the graph (creating nodes in the process)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 6)
G.add_edge(3, 7)

# Find a minimum vertex cover. This is a set of nodes such that each edge in the graph
# is incident to at least one node in the set. We use the approximation algorithm here.
vertex_cover = nx.algorithms.approximation.min_weighted_vertex_cover(G)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_nodes(G, pos, nodelist=vertex_cover, node_color='r')
nx.draw_networkx_nodes(G, pos, nodelist=set(G.nodes)-vertex_cover, node_color='b')
plt.show()