class TicTacToe:

    def __init__(self):
        # self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        # how to rewrite using comprehension?
        self.board = [[' ', ' ', ' '] for j in range(3)]
        self.player = 'X'

    def mark(self, i, j):
        if not(0 <= i <= 2 and 0 <= j <= 2):
            print('invalid board position')
        if self.board[i][j] != ' ':
            print('board position occupied')
        self.board[i][j] = self.player
        if self.is_win(self.player):
            print("winner is " + self.player)
            exit()

    #     switch the player
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def is_win(self, mark):
        return (mark == self.board[0][0] == self.board[0][1] == self.board[0][2] or # row 0
                mark == self.board[1][0] == self.board[1][1] == self.board[1][2] or # row 1
                mark == self.board[2][0] == self.board[2][1] == self.board[2][2] or # row 2
                mark == self.board[0][0] == self.board[1][0] == self.board[2][0] or # column 0
                mark == self.board[0][1] == self.board[1][1] == self.board[2][1] or # column 1
                mark == self.board[0][2] == self.board[1][2] == self.board[2][2] or # column 2
                mark == self.board[0][0] == self.board[1][1] == self.board[2][2] or # diagonal 1
                mark == self.board[0][2] == self.board[1][1] == self.board[2][0] # diagonal 2
            )

    def __str__(self):
        result = ""
        for row in self.board:
            result += " | ".join(row)
            result += "\n----------\n"
        return result


game = TicTacToe()
game.mark(1, 1)
print(game)
game.mark(1, 2)
print(game)
game.mark(2, 2)
print(game)
