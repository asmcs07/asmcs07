
import random


# The game board: It is usually square in shape, and contains cells for numbers. 
# Numbers: Each square contains a number that is a multiple of 2. 
#Moving numbers: Numbers can be moved either up, down, right or left. 
#Merging numbers: Numbers that are identical to each other are merged in the same row or column. 
#The primary goal: reaching the number 2048 or higher.
#Game Ending: The game ends if the board is filled with numbers and the player has no upcoming moves left.

class Game:
    def __init__(self):
        self.board = [[0 for i in range(4)] for j in range(4)]
        self.score = 0

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        random_cell = random.choice(empty_cells)
        self.board[random_cell[0]][random_cell[1]] = 2

    def can_move(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0 or (i > 0 and self.board[i][j] == self.board[i - 1][j]) or (j > 0 and self.board[i][j] == self.board[i][j - 1]):
                    return True
        return False

    def move(self, direction):
        if direction == "up":
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] != 0:
                        k = i
                        while k > 0 and self.board[k - 1][j] == 0:
                            self.board[k - 1][j] = self.board[k][j]
                            self.board[k][j] = 0
                            k -= 1
                        if k > 0 and self.board[k - 1][j] == self.board[k][j]:
                            self.board[k - 1][j] *= 2
                            self.board[k][j] = 0
                            self.score += self.board[k - 1][j]

        elif direction == "down":
            for i in range(3, -1, -1):
                for j in range(4):
                    if self.board[i][j] != 0:
                        k = i
                        while k < 3 and self.board[k + 1][j] == 0:
                            self.board[k + 1][j] = self.board[k][j]
                            self.board[k][j] = 0
                            k += 1
                        if k < 3 and self.board[k + 1][j] == self.board[k][j]:
                            self.board[k + 1][j] *= 2
                            self.board[k][j] = 0
                            self.score += self.board[k + 1][j]

        elif direction == "left":
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] != 0:
                        k = j
                        while k > 0 and self.board[i][k - 1] == 0:
                            self.board[i][k - 1] = self.board[i][k]
                            self.board[i][k] = 0
                            k -= 1
                        if k > 0 and self.board[i][k - 1] == self.board[i][k]:
                            self.board[i][k - 1] *= 2
                            self.board[i][k] = 0
                            self.score += self.board[i][k - 1]

        elif direction == "right":
            for i in range(4):
                for j in range(3, -1, -1):
                    if self.board[i][j] != 0:
                        k = j
                        while k < 3 and self.board[i][k + 1] == 0:
                            self.board[i][k + 1] = self.board[i][k]
                            self.board[i][k] = 0
                            k += 1
                        if k < 3 and self.board[i][k + 1] == self.board[i][k]:
                            self.board[i][k + 1] *= 2
                            self.board[i][k] = 0
                            self.score += self.board[i][k + 1]

    def is_game_over(self):
        return not self.
