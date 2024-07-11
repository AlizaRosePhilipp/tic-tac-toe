
from django.db import models


class Game(models.Model):
    board = models.CharField(max_length=9, default='-'*9)  # Represents the 3x3 game board as a string
    current_turn = models.CharField(max_length=1, default='X')  # Current player turn ('X' or 'O')
    winner = models.CharField(max_length=1, null=True, blank=True)  # Winner ('X', 'O', or None)

    def __str__(self):
        return f"Game {self.id}"