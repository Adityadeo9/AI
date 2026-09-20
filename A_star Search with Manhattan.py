import heapq

# Grid coordinates
graph = {
    (0, 0): [(0, 1), (1, 0)],
    (0, 1): [(0, 0), (0, 2), (1, 1)],
    (0, 2): [(0, 1), (1, 2)],
    (1, 0): [(0, 0), (1, 1), (2, 0)],
    (1, 1): [(0, 1), (1, 0), (1, 2), (2, 1)],
    (1, 2): [(0, 2), (1, 1), (2, 2)],
    (2, 0): [(1, 0), (2, 1)],
    (2, 1): [(2, 0), (1, 1), (2, 2)],
    (2, 2): [(1, 2), (2, 1)]
}

start = (0, 0)
goal = (2, 2)

# Manhattan distance
def heuristic(node):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

queue = []

heapq.heappush(queue, (heuristic(start), 0, start, [start]))

visited = set()

while queue:
    f, cost, node, path = heapq.heappop(queue)

    if node == goal:
        print("Path found:")
        print(path)
        print("Total cost:", cost)
        break

    if node in visited:
        continue

    visited.add(node)

    for neighbour in graph[node]:

        new_cost = cost + 1
        new_f = new_cost + heuristic(neighbour)

        heapq.heappush(
            queue,
            (new_f, new_cost, neighbour, path + [neighbour])
        )