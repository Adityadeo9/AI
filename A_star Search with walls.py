import heapq

# Grid size
rows = 5
cols = 5

# Start and goal
start = (0, 0)
goal = (4, 4)

# Walls / blocked cells
walls = {
    (1, 1),
    (1, 2),
    (2, 2),
    (3, 2)
}

# Manhattan distance
def heuristic(node):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# Find neighbours
def get_neighbours(node):

    r, c = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbours = []

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if nr >= 0 and nr < rows and nc >= 0 and nc < cols:

            if (nr, nc) not in walls:
                neighbours.append((nr, nc))

    return neighbours


queue = []

heapq.heappush(
    queue,
    (heuristic(start), 0, start, [start])
)

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

    for neighbour in get_neighbours(node):

        new_cost = cost + 1

        new_f = new_cost + heuristic(neighbour)

        heapq.heappush(
            queue,
            (new_f, new_cost, neighbour, path + [neighbour])
        )