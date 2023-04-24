from heapq import heappush, heappop


def get_neigh_nodes(grid, x, y):
    check_valid = lambda x, y: True if 0 <= x < len(grid[0]) and 0 <= y < len(grid) else False
    ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    return [((x+dx, y+dy), grid[y+dy][x+dx]) for dx, dy in ds if check_valid(x+dx, y+dy)]


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def A_star(grid, start, goal):
    graph = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            graph[ (x, y) ] = graph.get ( (x, y), [ ] ) + get_neigh_nodes (grid, x, y )

    queue = []
    heappush(queue, (0, start))
    visited = {start: None}
    cost_visited = {start: 0}

    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == goal:
            queue = []
            continue

        neigh_nodes = graph[cur_node]
        for neigh in neigh_nodes:
            neigh_node, neigh_cost = neigh
            new_cost = neigh_cost + cost_visited[cur_node]

            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + heuristic(neigh_node, goal)
                heappush(queue, (priority, neigh_node))
                visited[neigh_node] = cur_node
                cost_visited[neigh_node] = new_cost

    way = []
    cost = 0
    cur = goal
    while cur is not None:
        way.append(cur)
        cost += cost_visited[cur]
        cur = visited[cur]

    return way[::-1], cost


