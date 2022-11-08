'''
write a class called tic tac toe

1. function to control the overall program running
2. start of the game -> constructor
    - board: dictionary {0: ' ', 1: ' ' }
             2d list(3x3)
             1d list(9)
    - mark: X or O
3. print board
4. player turn (player enter position)
5. check for end condition
'''
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.player_mark = 'X'

    def mark(self, i):
        if 0 <= i <= 8 and self.board[i] == ' ':
            self.board[i] = self.player_mark
        else:
            print('invalid move')
            return
        
        # switch the player mark
        if self.player_mark == 'X':
            self.player_mark = 'O'
        else:
            self.player_mark = 'X'

    # check 3 rows, 3 columns and 3 diagonals are in same mark
    def is_win(self, mark):
        return (mark == self.board[0] == self.board[1] == self.board[2] or
                mark == self.board[3] == self.board[4] == self.board[5] or
                mark == self.board[6] == self.board[7] == self.board[8] or
                mark == self.board[0] == self.board[3] == self.board[6] or
                mark == self.board[1] == self.board[4] == self.board[7] or
                mark == self.board[2] == self.board[5] == self.board[8] or
                mark == self.board[0] == self.board[4] == self.board[8] or
                mark == self.board[2] == self.board[4] == self.board[6])

    # run out of the space, no one wins the game
    def is_even(self):
        for element in self.board:
            if element == ' ':
                return False
        return True

    # [' ', ]
    def print_board(self):
        result = ''
        col = 0
        for row in self.board:
            if col == 2:
                result += row + '\n'
                col = 0
            else:
                result += row + ' | '
                col += 1

        print(result)


tic_tac_toe = TicTacToe()
win = False

while not win:
    tic_tac_toe.print_board()
    step = int(input('enter the position number from 0 to 8: '))
    mark = tic_tac_toe.player_mark
    tic_tac_toe.mark(step)
    if tic_tac_toe.is_win(mark):
        print(mark + " wins the game")
        break
    elif tic_tac_toe.is_even():
        print("game is even, finished")
        break

# # create an array with n same values
# s = [1] * 9
# print(s)
'''
So far, you have all the pieces for this game, the remaining part is to write a main game loop,
where each player takes turn to enter a mark, you place the mark and check who win the game
'''



# s = "I'm a student"
# s = '''he said:"I'am ok"'''
# s[0]
# print(len(s))

