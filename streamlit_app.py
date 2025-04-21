import streamlit as st
import heapq

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

# Dijkstra's algorithm
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

# Streamlit UI
st.title("🚗 Shortest Path Finder")
start = st.sidebar.selectbox("Select starting town:", list(graph.keys()))
end = st.sidebar.selectbox("Select destination town:", list(graph.keys()))

if st.sidebar.button("Find Shortest Path"):
    path, distance = dijkstra(graph, start, end)
    if path:
        st.success(f"Shortest path from {start} to {end}: {' → '.join(path)} (Distance: {distance} miles)")
    else:
        st.error("No path found between the selected towns.")
