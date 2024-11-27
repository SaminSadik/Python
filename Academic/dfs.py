def dfs(graph, node, visited):
    # Only visit the node if it's not visited yet
    if node not in visited:
        print(node, end=" ")
        visited.add(node)  # Mark the node as visited
        # Recurse for each neighbor
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

def graph_input():
    graph = {}
    edges = int(input("Enter the number of edges in your graph: "))
    print("Enter the Edges (node1 node2): ")
    for _ in range(edges):
        u, v = input().split()
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # To make the graph undirected
    return graph

graph = graph_input()
start = input("Enter the starting node for DFS: ")
visited = set()

print("Depth-First Search Traversal: ")
dfs(graph, start, visited)
print()