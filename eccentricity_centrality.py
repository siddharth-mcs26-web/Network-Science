def Calculate_eccentricity(nodes, edges, node=None):
    adjacency_list = {node: set() for node in nodes}

    for u, v in edges:
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)

    eccentricity = {}
    eccentricity_centrality = {}

# 3. Perform BFS for Every Node to Compute Eccentricity
    for source_node in nodes:
        # Reset distances for each BFS run
        distances = {node: float("inf") for node in nodes}
        distances[source_node] = 0

        visited = set([source_node])
        queue = deque([source_node])

        while queue:
            current_node = queue.popleft()

            for neighbor in adjacency_list[current_node]:
                if neighbor not in visited:
                    distances[neighbor] = distances[current_node] + 1
                    visited.add(neighbor)
                    queue.append(neighbor)  # Enqueue neighbor to continue traversal

        # Eccentricity = Maximum shortest-path distance from source_node
        max_distance = max(distances.values())
        eccentricity[source_node] = max_distance

        # Eccentricity Centrality = Reciprocal of Eccentricity
        eccentricity_centrality[source_node] = round(1.0 / max_distance, 4)
    
    if node is not None:
        return eccentricity_centrality[node], eccentricity[node]
    return eccentricity_centrality, eccentricity
