'''
0: A
1: B
2: C
3: D
'''
import heapq
# graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
# # check if bc is connected
# graph[1][2]
from collections import deque
import sys

class Graph:
    def __init__(self):
        self.graph = {}
        self.value = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
            self.value[vertex1] = {vertex2: weight}
            self.value[vertex2] = {vertex1: weight}

    def show(self):
        for vertex in self.graph:
            print(vertex, ' -> ', ' '.join(map(str, self.graph[vertex])))

    def bfs(self, start_vertex):
        visited = set()
        queue = deque()
        queue.append(start_vertex)

        while queue:
            current = queue.popleft()
            if current not in visited:
                print(current)
                visited.add(current)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    def dfs_iterative(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            current = stack.pop()
            if current not in visited:
                print(current)
                visited.add(current)
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    def dfs(self, start_vertex):
        visited = set()

        def dfs_recursive(current):
            visited.add(current)
            print(current)

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)

    def dijkstra(self, start):
        unvisited_nodes = list(self.graph.keys())
        shortest_path = {}
        previous_nodes = {}
        
        for node in unvisited_nodes:
            shortest_path[node] = sys.maxsize
        shortest_path[start] = 0

        # run dijkstra until all visit all nodes
        while unvisited_nodes:
            current = unvisited_nodes[0]
            # find current nodes from unvisited nodes whose shortest distance is min
            for node in unvisited_nodes:
                if shortest_path[node] < shortest_path[current]:
                    current = node

            # update current node's neighbors shortest path
            neighbors = self.graph[current]
            for neighbor in neighbors:
                weight = self.value[current][neighbor]
                tmp = weight + shortest_path[current]
                if tmp < shortest_path[neighbor]:
                    shortest_path[neighbor] = tmp
                    previous_nodes[neighbor] = current
            
            unvisited_nodes.remove(current)

    def prim(self, start_vertex):
        mst = []
        visited = set()
        heap = [(0, start_vertex)]
        total_cost = 0

        while heap:
            cost, current_vertex = heapq.heappop(heap)
            if current_vertex not in visited:
                visited.add(current_vertex)
                mst.append(self.graph[current_vertex])
                total_cost += cost

                for neighbor, neighbor_cost in self.graph[current_vertex]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (neighbor_cost, neighbor))

        return mst


graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')

graph.show()
graph.bfs('A')