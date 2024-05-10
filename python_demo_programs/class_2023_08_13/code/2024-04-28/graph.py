class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)

    def dfs(self, start_vertex, visited, res):
        visited.add(start_vertex)
        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, res)

        res.append(start_vertex)

    def topologial_sort(self):
        visited = set()
        res = []

        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex, visited, res)

        res = res[::-1]
        print(res)