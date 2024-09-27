import matplotlib.pyplot as plt
import networkx as nx

# Creating a directed graph to represent the cascading effects
G = nx.DiGraph()

# Adding nodes with their respective positions and colors for visualization
nodes = {
    "Water Plant": {"pos": (0, 0), "color": 'lightblue'},
    "Aquatic Life/Organisms": {"pos": (-2, -1), "color": 'lightgreen'},
    "Urban Water Supply": {"pos": (2, -1), "color": 'yellow'},
    "Biodiversity": {"pos": (-3, -2), "color": 'green'},
    "Public Health": {"pos": (3, -2), "color": 'orange'},
    "Ecological Balance": {"pos": (-1, -2), "color": 'pink'},
    "Water Quality": {"pos": (1, -3), "color": 'purple'},
    "Economic Impact": {"pos": (3, -3), "color": 'red'},
    "Recreational Activities": {"pos": (-3, -3), "color": 'blue'},
    "Agricultural Usage": {"pos": (-1, -3), "color": 'brown'},
    "Industrial Demand": {"pos": (1, -2), "color": 'grey'},
    "Energy Conservation": {"pos": (2, -2), "color": 'magenta'},
    "Habitat Conservation": {"pos": (-2, -2), "color": 'cyan'}
}

# Adding nodes and their attributes to the graph
for node, attr in nodes.items():
    G.add_node(node, **attr)

# Defining the edges that connect these nodes, representing cascading effects
edges = [
    ("Water Plant", "Aquatic Life/Organisms"),
    ("Water Plant", "Urban Water Supply"),
    ("Water Plant", "Agricultural Usage"),
    ("Water Plant", "Industrial Demand"),
    ("Aquatic Life/Organisms", "Biodiversity"),
    ("Urban Water Supply", "Public Health"),
    ("Urban Water Supply", "Economic Impact"),
    ("Urban Water Supply", "Recreational Activities"),
    ("Biodiversity", "Ecological Balance"),
    ("Ecological Balance", "Water Quality"),
    ("Public Health", "Ecological Balance"),
    ("Economic Impact", "Energy Conservation"),
    ("Recreational Activities", "Habitat Conservation"),
    ("Agricultural Usage", "Economic Impact"),
    ("Industrial Demand", "Energy Conservation"),
    ("Habitat Conservation", "Biodiversity"),
    ("Energy Conservation", "Public Health")
]

# Adding edges to the graph
G.add_edges_from(edges)

# Extracting positions and colors for drawing
pos = nx.get_node_attributes(G, 'pos')
colors = [attr['color'] for node, attr in G.nodes(data=True)]

# Make the "Energy Conservation" node larger and stand out
node_sizes = [5000 if node == "Energy Conservation" else 3000 for node in G.nodes]
node_shapes = {node: 'o' for node in G.nodes}  # Default shape is 'o' (circle)
node_shapes["Energy Conservation"] = 'D'  # Diamond shape for "Energy Conservation"

# Drawing the graph
plt.figure(figsize=(14, 12))
nx.draw(G, pos, with_labels=True, node_color=colors, node_size=node_sizes, edge_color='gray', font_size=12, font_weight='bold', arrowstyle='-|>', arrowsize=20)

# Highlight the "Energy Conservation" node with a different shape
nx.draw_networkx_nodes(G, pos, nodelist=["Energy Conservation"], node_shape='D', node_size=5000, node_color='magenta')

plt.title('Cascading Effects of the Water Treatment Plant', size=15, color='blue')
plt.show()
