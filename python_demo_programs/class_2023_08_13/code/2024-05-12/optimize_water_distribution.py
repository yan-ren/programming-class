from typing import List
import heapq


def min_cost_to_supply_water(n: int, wells: List[int], pipes: List[List[int]]):
    graph = [[] for i in range(n + 1)]
    heap = []

    # create graph using adjacent list
    for u, v, w in pipes:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # create additional vertex and add edges to all existing nodes
    graph[0] = []
    well_index = 1
    for well_cost in wells:
        graph[0].append((well_index, well_cost))
        heapq.heappush(heap, (well_cost, well_index))
        well_index += 1

    seen = set()
    total_cost = 0
    # prim algorithm for MST
    while heap:
        cost, vertex = heapq.heappop(heap)
        if vertex in seen:
            continue
        seen.add(vertex)
        total_cost += cost
        for neighbor, weight in graph[vertex]:
            if neighbor not in seen:
                heapq.heappush(heap, (weight, neighbor))

    return total_cost


print(min_cost_to_supply_water(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]]))
