from django.http import JsonResponse
from django.shortcuts import render

from .models import Game

# In-memory game instance (for demonstration, in production use a database)
game_instance = Game()


def game_board(request):
    board = game_instance.board
    return JsonResponse({'board': board, 'current_turn': game_instance.current_turn, 'winner': game_instance.winner})


def make_move(request):
    if request.method == 'POST':
        data = request.POST
        row = int(data['row'])
        col = int(data['col'])
        if game_instance.make_move(row, col):
            return JsonResponse({'status': 'Move successful'})
        else:
            return JsonResponse({'error': 'Invalid move or game already won'})
    else:
        return JsonResponse({'error': 'Invalid request method'})




