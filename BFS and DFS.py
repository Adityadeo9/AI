# BFS and DFS Tree Traversal

from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}


# Breadth First Search
def bfs(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return result


# Depth First Search
def dfs(node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbour in graph[node]:
        if neighbour not in visited:
            result.extend(dfs(neighbour, visited))

    return result


print("BFS Traversal:")
print(bfs(1))

print("\nDFS Traversal:")
print(dfs(1))