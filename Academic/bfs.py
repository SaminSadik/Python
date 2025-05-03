def bfs(graph, start):
    visited, queue = set([start]), [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def graph_input(graph = {}):
    edges = int(input("Enter the number of edges in your graph: "))
    print("Enter the Edges (node1 node2): ")
    for _ in range(edges):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph

graph = graph_input()
start = input("Enter the starting node for BFS: ")
print("Breadth-First Search Traversal: ")
bfs(graph, start)
print()