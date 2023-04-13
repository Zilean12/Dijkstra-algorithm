# dijkstra algorithm

import heapq

def dijkstra(graph, start):
    
    distance = {node: float('inf') for node in graph.keys()}
    previous = {node: None for node in graph}

    distance[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distance[current_node]:
            continue

        for adjacent, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < distance[adjacent]:
                distance[adjacent] = new_dist
                previous[adjacent] = current_node
                heapq.heappush(pq, (new_dist, adjacent))

    return distance, previous


# example usage
graph = {
    '1': [('2', 6), ('3', 5), ('4',5)],
    '2': [('5', 1)],
    '3': [('2', 2), ('5', 1)],
    '4': [('3', 2),('6', 1)],
    '5': [('7',3)],
    '6': [('7',3)],
    '7': [('7',0)]

}

start_node = '1'
distance, previous = dijkstra(graph, start_node)

# print the shortest path from start_node to all other nodes
for node, dist in distance.items():
    path = []
    curr_node = node
    while curr_node != start_node:
        path.append(curr_node)
        curr_node = previous[curr_node]
    path.append(start_node)
    path.reverse()
    print(f"Shortest path from {start_node} to {node}: {' -> '.join(path)}, cost: {dist}")
