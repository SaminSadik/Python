def dfs(graph, node, visited=None):
    if visited is None: visited = set()
    if node in visited:
        return
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph.get(node, []):
        dfs(graph, neighbor, visited)

def graph_input(graph = {}):
    edges = int(input("Enter the number of edges in your graph: "))
    print("Enter the Edges (node1 node2): ")
    for _ in range(edges):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph


graph = graph_input()
start = input("Enter the starting node for DFS: ")
print("Depth-First Search Traversal: ")
dfs(graph, start)
print()
