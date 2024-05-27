from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            # mark current position as visited by using 'E'
            board[r][c] = 'E'
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        def bfs(r, c):
            if board[r][c] != 'O':
                return

            queue = []
            queue.append((r, c))

            while queue:
                x, y = queue.pop(0)
                board[x][y] = 'E'
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    next_x, next_y = x + dx, y + dy
                    # check if go beyond the boarder
                    if 0 <= next_x < rows and 0 <= next_y < cols and board[next_x][next_y] == 'O':
                        queue.append((next_x, next_y))


        # mark the boarder 'O' and use dfs to find all connected 'O'
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        for j in range(cols):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[rows-1][j] == 'O':
                dfs(rows - 1, j)

        # flip the 'O' to 'X' and revert 'E' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] == 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
