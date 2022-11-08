'''
we want to write a program that stores a sequence of high score entries for a video game
This is representative of many applications in which a sequence of objects must be stored

'''
class Entry:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Scoreboard:
    def __init__(self, capacity=10):
        self._board = []
        self._capacity = capacity
        self._n = 0 # number of actual entries

    def get_item(self, k):
        if k > len(self._board):
            return None

        return self._board[k]

    def add_item(self, entry):
        '''add score to the _board only if score belongs to the highest score'''
        if len(self._board) < self._capacity:
            self._board.append(entry)
            return False
        else:
            j = 0
            min_index = j
            min_score = self._board[j].score
            while j < len(self._board):
                if self._board[j].score < min_score:
                    min_index = j
                    min_score = self._board[j].score
            self._board[min_index] = entry
            return True
        return False


entry1 = Entry("Tom", 20)
entry2 = Entry("Kim", 21)
entry3 = Entry("Jim", 22)
entry4 = Entry("Bob", 1)
score_board = Scoreboard(3)
score_board.add_item(entry1)
score_board.add_item(entry2)
score_board.add_item(entry3)
score_board.add_item(entry4)
'''             
[5, 3, 6]

add 2? no
add 4?
remove 3
then add 4
[5, 6, 4]

add 7?
remove 4, then add 7

'''

