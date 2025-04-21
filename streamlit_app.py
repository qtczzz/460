import streamlit as st
import heapq
import plotly.graph_objects as go
# Define distance data between towns (fictional)
graph = {
    "Chicago": {"McLain": 40, "Aurora": 60, "Parker": 50},
    "McLain": {"Aurora": 10, "Smallville": 70},
    "Aurora": {"Parker": 20, "Smallville": 55, "Farmer": 40},
    "Parker": {"Farmer": 50},
    "Smallville": {"Farmer": 10, "Bayview": 60},
    "Farmer": {"Bayview": 80},
    "Bayview": {}
}
# Fixed coordinates for visualization
positions = {
    "Chicago": (0, 0),
    "McLain": (1, 1),
    "Aurora": (2, 0),
    "Parker": (3, 1),
    "Smallville": (2, -1),
    "Farmer": (4, 0),
    "Bayview": (5, 0)
}

# Dijkstra algorithm
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return (path, cost)
        for adj, weight in graph.get(node, {}).items():
            if adj not in visited:
                heapq.heappush(queue, (cost + weight, adj, path))
    return ([], float("inf"))

# Streamlit app
st.title("📍 Town Path Visualizer with Shortest Route")

start = st.sidebar.selectbox("Start Town:", list(graph.keys()))
end = st.sidebar.selectbox("End Town:", list(graph.keys()))

if st.sidebar.button("Find Shortest Path"):
    path, distance = dijkstra(graph, start, end)
    if not path:
        st.error("No path found!")
    else:
        st.success(f"Shortest path: {' → '.join(path)} (Distance: {distance} miles)")

        # Plot graph
        fig = go.Figure()

        # All edges
        for town, neighbors in graph.items():
            for neighbor, dist in neighbors.items():
                x0, y0 = positions[town]
                x1, y1 = positions[neighbor]
                fig.add_trace(go.Scatter(
                    x=[x0, x1], y=[y0, y1],
                    mode='lines',
                    line=dict(color='gray', width=2),
                    hoverinfo='text',
                    text=[f"{town} → {neighbor}: {dist} mi"]
                ))

        # Shortest path edges in red
        for i in range(len(path) - 1):
            t0, t1 = path[i], path[i+1]
            x0, y0 = positions[t0]
            x1, y1 = positions[t1]
            fig.add_trace(go.Scatter(
                x=[x0, x1], y=[y0, y1],
                mode='lines',
                line=dict(color='red', width=4),
                hoverinfo='text',
                text=[f"{t0} → {t1}"]
            ))

        # Nodes
        for town, (x, y) in positions.items():
            fig.add_trace(go.Scatter(
                x=[x], y=[y],
                mode='markers+text',
                marker=dict(size=10, color='lightblue'),
                text=[town],
                textposition='top center'
            ))

        fig.update_layout(showlegend=False, height=600)
        st.plotly_chart(fig)
