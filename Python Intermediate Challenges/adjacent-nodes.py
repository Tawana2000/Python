# Write a function to find all the adjacent nodes of a given node in a graph

def find_adjacent_nodes(graph, node):
    
    node = str(node)
    if node not in graph:
        return []
    
    return graph[node]

graph = graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(find_adjacent_nodes(graph, 'A'))