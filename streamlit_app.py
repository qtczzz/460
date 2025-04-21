
import streamlit as st

import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Define distance data (fictional) between adjacent towns
edges = [
    ("Chicago", "McLain", 40),
    ("Chicago", "Aurora", 60),
    ("McLain", "Aurora", 10),
    ("Chicago", "Parker", 50),
    ("Chicago", "Smallville", 70),
    ("Aurora", "Parker", 20),
    ("Aurora", "Smallville", 55),
    ("Aurora", "Farmer", 40),
    ("Parker", "Farmer", 50),
    ("Smallville", "Farmer", 10),
    ("Farmer", "Bayview", 60),
    ("Smallville", "Bayview", 80),
]

# Build graph
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Sidebar inputs
st.sidebar.title("Shortest Path Finder")
start = st.sidebar.selectbox("Select starting town:", sorted(G.nodes))
end = st.sidebar.selectbox("Select destination town:", sorted(G.nodes))

# Display shortest path
if st.sidebar.button("Find Shortest Path"):
    try:
        path = nx.shortest_path(G, source=start, target=end, weight='weight')
        distance = nx.shortest_path_length(G, source=start, target=end, weight='weight')
        st.success(f"Shortest path from {start} to {end}: {' → '.join(path)} (Distance: {distance} miles)")
    except nx.NetworkXNoPath:
        st.error("No path exists between the selected towns.")

# Optional: Visualize the graph
st.write("### Town Network Map")
fig, ax = plt.subplots(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d} mi" for u, v, d in G.edges(data='weight')}, ax=ax)
st.pyplot(fig)
