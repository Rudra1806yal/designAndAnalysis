pip install networkx

#it is used to generate graph in the VS Code Jupyter Notebook
%matplotlib inline

#Implementing the library
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import heapq
import time
import random
from collections import deque
print("Traffic Management System")
print("All libraries imported successfully!")

# Create an empty graph
G = nx.Graph()

# Add intersections
intersections = ["A", "B", "C", "D", "E"]

G.add_nodes_from(intersections)

# Add roads with distance and travel time
roads = [
    ("A", "B", 4, 5),
    ("A", "C", 2, 3),
    ("B", "C", 1, 2),
    ("B", "D", 5, 7),
    ("C", "D", 8, 10),
    ("C", "E", 10, 12),
    ("D", "E", 2, 3)
]

for u, v, distance, travel_time in roads:
    G.add_edge(
        u, v,
        distance=distance,
        time=travel_time
    )

print("Road network created successfully!")
print("Intersections:", G.number_of_nodes())
print("Roads:", G.number_of_edges())

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(10, 6))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=1500,
    font_size=12,
    font_weight="bold"
)

edge_labels = nx.get_edge_attributes(G, "time")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels
)

plt.title("City Road Network")
plt.show()

adj_list = {}

for node in G.nodes():
    adj_list[node] = []

    for neighbor in G.neighbors(node):
        weight = G[node][neighbor]["time"]
        adj_list[node].append((neighbor, weight))

print("Adjacency List:")

for node, neighbors in adj_list.items():
    print(node, ":", neighbors)

adj_matrix = nx.to_numpy_array(
    G,
    nodelist=sorted(G.nodes()),
    weight="time"
)

adj_df = pd.DataFrame(
    adj_matrix,
    index=sorted(G.nodes()),
    columns=sorted(G.nodes())
)

print("Adjacency Matrix:")
display(adj_df)

def dijkstra(graph, source):

    distance = {
        node: float("inf")
        for node in graph.nodes()
    }

    parent = {
        node: None
        for node in graph.nodes()
    }

    distance[source] = 0

    pq = [(0, source)]
    visited = set()

    while pq:

        current_distance, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        for v in graph.neighbors(u):

            weight = graph[u][v]["time"]

            new_distance = current_distance + weight

            if new_distance < distance[v]:

                distance[v] = new_distance
                parent[v] = u

                heapq.heappush(
                    pq, (new_distance, v)
                )

    return distance, parent

source = "A"
destination = "E"

distance, parent = dijkstra(G, source)

path = []
current = destination

while current is not None:
    path.append(current)
    current = parent[current]

path.reverse()

if path[0] == source:
    print("Shortest Route:", " -> ".join(path))
    print("Total Travel Time:", distance[destination], "minutes")
else:
    print("No route found")

route_edges = list(zip(path[:-1], path[1:]))

plt.figure(figsize=(10, 6))

nx.draw(
    G, pos,
    with_labels=True,
    node_color="skyblue",
    node_size=1500
)

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=route_edges,
    edge_color="red",
    width=4
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=nx.get_edge_attributes(G, "time")
)

plt.title("Dijkstra Shortest Route")
plt.show()

def bellman_ford(graph, source):

    distance = {
        node: float("inf")
        for node in graph.nodes()
    }

    parent = {
        node: None
        for node in graph.nodes()
    }

    distance[source] = 0

    edges = []

    for u, v, data in graph.edges(data=True):
        weight = data["time"]

        edges.append((u, v, weight))
        edges.append((v, u, weight))

    trace = []

    for i in range(len(graph.nodes()) - 1):

        updated = False

        for u, v, weight in edges:

            if distance[u] != float("inf"):

                new_distance = distance[u] + weight

                if new_distance < distance[v]:

                    distance[v] = new_distance
                    parent[v] = u
                    updated = True

        trace.append({
            "Pass": i + 1,
            **distance.copy()
        })

        if not updated:
            break

    negative_cycle = any(
        distance[u] != float("inf")
        and distance[u] + weight < distance[v]
        for u, v, weight in edges
    )

    return distance, parent, trace, negative_cycle

# Store original travel times
original_times = {
    (u, v): data["time"]
    for u, v, data in G.edges(data=True)
}

# Increase travel time on road A-C
G["A"]["C"]["time"] = 20

print("Traffic congestion simulated!")
print("Road A-C travel time:", G["A"]["C"]["time"])

distance, parent, trace, negative_cycle = bellman_ford(G, "A")

if negative_cycle:
    print("Negative cycle detected!")
else:
    destination = "E"

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Updated Route:", " -> ".join(path))
    print("Updated Travel Time:", distance[destination])

    display(pd.DataFrame(trace))

def bfs(graph, start):

    visited = set([start])
    queue = deque([start])

    traversal = []

    while queue:

        node = queue.popleft()
        traversal.append(node)

        for neighbor in sorted(graph.neighbors(node)):

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


print("BFS Traversal:", bfs(G, "A"))

def dfs(graph, start):

    visited = set()
    traversal = []

    def visit(node):

        visited.add(node)
        traversal.append(node)

        for neighbor in sorted(graph.neighbors(node)):

            if neighbor not in visited:
                visit(neighbor)

    visit(start)

    return traversal


print("DFS Traversal:", dfs(G, "A"))

def prim(graph):

    start = list(graph.nodes())[0]

    visited = {start}

    pq = []

    for neighbor in graph.neighbors(start):

        weight = graph[start][neighbor]["distance"]

        heapq.heappush(
            pq, (weight, start, neighbor)
        )

    mst = []
    total_cost = 0

    while pq and len(visited) < len(graph.nodes()):

        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)

        mst.append((u, v, weight))
        total_cost += weight

        for neighbor in graph.neighbors(v):

            if neighbor not in visited:

                w = graph[v][neighbor]["distance"]

                heapq.heappush(
                    pq, (w, v, neighbor)
                )

    if len(visited) != len(graph.nodes()):
        raise ValueError("Network is disconnected.")

    return mst, total_cost


prim_mst, prim_cost = prim(G)

print("Prim MST:")
display(pd.DataFrame(
    prim_mst,
    columns=["Road 1", "Road 2", "Distance"]
))

print("Total Infrastructure Cost:", prim_cost)

def kruskal(graph):

    parent = {node: node for node in graph.nodes()}
    rank = {node: 0 for node in graph.nodes()}

    def find(x):

        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union(a, b):

        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        if rank[root_a] < rank[root_b]:
            root_a, root_b = root_b, root_a

        parent[root_b] = root_a

        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1

        return True

    sorted_edges = sorted(
        graph.edges(data=True),
        key=lambda x: x[2]["distance"]
    )

    mst = []
    total_cost = 0

    for u, v, data in sorted_edges:

        weight = data["distance"]

        if union(u, v):

            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == len(graph.nodes()) - 1:
                break

    if len(mst) != len(graph.nodes()) - 1:
        raise ValueError("Network is disconnected.")

    return mst, total_cost


kruskal_mst, kruskal_cost = kruskal(G)

print("Kruskal MST:")
display(pd.DataFrame(
    kruskal_mst,
    columns=["Road 1", "Road 2", "Distance"]
))

print("Total Infrastructure Cost:", kruskal_cost)

def generate_network(n):

    graph = nx.Graph()

    graph.add_nodes_from(range(n))

    # Ensure the graph is connected
    for i in range(1, n):

        parent = random.randrange(i)

        graph.add_edge(
            i, parent,
            distance=random.randint(1, 20),
            time=random.randint(1, 20)
        )

    # Add additional roads
    for _ in range(n):

        u, v = random.sample(range(n), 2)

        graph.add_edge(
            u, v,
            distance=random.randint(1, 20),
            time=random.randint(1, 20)
        )

    return graph

sizes = [10, 25, 50, 100]

results = []

for n in sizes:

    test_graph = generate_network(n)

    algorithms = {
        "BFS": lambda: nx.bfs_tree(test_graph, 0),
        "DFS": lambda: nx.dfs_tree(test_graph, 0),
        "Dijkstra": lambda: nx.single_source_dijkstra_path_length(
            test_graph, 0, weight="time"
        ),
        "Bellman-Ford": lambda: nx.single_source_bellman_ford_path_length(
            test_graph, 0, weight="time"
        ),
        "Prim": lambda: nx.minimum_spanning_tree(
            test_graph, algorithm="prim", weight="distance"
        ),
        "Kruskal": lambda: nx.minimum_spanning_tree(
            test_graph, algorithm="kruskal", weight="distance"
        )
    }

    for name, function in algorithms.items():

        start_time = time.perf_counter()

        function()

        end_time = time.perf_counter()

        execution_time = (end_time - start_time) * 1000

        results.append({
            "Intersections": n,
            "Roads": test_graph.number_of_edges(),
            "Algorithm": name,
            "Execution Time (ms)": execution_time
        })


results_df = pd.DataFrame(results)

display(results_df)

for algorithm in results_df["Algorithm"].unique():

    data = results_df[
        results_df["Algorithm"] == algorithm
    ]

    plt.plot(
        data["Intersections"],
        data["Execution Time (ms)"],
        marker="o",
        label=algorithm
    )

plt.xlabel("Number of Intersections")
plt.ylabel("Execution Time (ms)")
plt.title("Graph Algorithm Performance Comparison")

plt.legend()
plt.grid()
plt.show()
