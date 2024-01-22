from typing import List


class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        number_of_prerequisites = [0] * n
        visited = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            graph[prerequisite].append(course)
            number_of_prerequisites[course] += 1

        queue = deque()
        for i in range(n):
            if number_of_prerequisites[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            visited.append(current)

            for next_course in graph[current]:
                number_of_prerequisites[next_course] -= 1
                if number_of_prerequisites[next_course] == 0:
                    queue.append(next_course)

        return len(visited) == n