from django.db import models


class Game:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_turn = 'X'
        self.winner = None

    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.winner:
            self.board[row][col] = self.current_turn
            if self.check_winner(row, col):
                self.winner = self.current_turn
            else:
                self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            return True
        return False

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_turn:
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_turn:
            return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_turn or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_turn):
            return True
        return False