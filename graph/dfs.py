graph = {
    "A": ["A", "D", "E"],
    "B": ["A", "C", "E"],
    "C": ["B", "G"],
    "D": ["A", "F"],
    "E": ["A", "B", "F"],
    "F": ["D", "E", "G"],
    "G": ["C", "F"]
}

def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor, visited)

# Driver code
visited = set()
start_node = "A"

print("DFS Traversal:")
dfs(start_node, visited)