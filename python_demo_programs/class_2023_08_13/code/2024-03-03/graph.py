'''
0: A
1: B
2: C
3: D
'''
# graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
# # check if bc is connected
# graph[1][2]
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

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