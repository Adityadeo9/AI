import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 2,
    'G': 0
}


def a_star(start, goal):

    queue = []

    heapq.heappush(queue, (0, start))

    cost = {start: 0}
    parent = {start: None}

    while queue:

        f, current = heapq.heappop(queue)

        if current == goal:
            break

        for neighbour, edge_cost in graph[current]:

            new_cost = cost[current] + edge_cost

            if neighbour not in cost or new_cost < cost[neighbour]:

                cost[neighbour] = new_cost

                f = new_cost + heuristic[neighbour]

                heapq.heappush(queue, (f, neighbour))

                parent[neighbour] = current

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("Path:", path)
    print("Total Cost:", cost[goal])


start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

a_star(start, goal)