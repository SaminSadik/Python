def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def graph_input():
    graph = {}
    edges = int(input("Enter the number of edges: "))
    
    for _ in range(edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

graph = graph_input()
start = input("Enter the starting node for BFS: ")

print("Breadth-First Search Traversal:")
bfs(graph, start)
print()