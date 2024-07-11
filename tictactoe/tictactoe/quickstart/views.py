from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Game


class GameStartView(APIView):
    def post(self, request):
        game = Game.objects.create()  # Create a new game instance
        return Response({'message': 'Game started successfully.', 'game_id': game.id}, status=status.HTTP_201_CREATED)


class GameMoveView(APIView):
    def put(self, request):
        game_id = request.data.get('game_id')
        position = int(request.data.get('position'))

        try:
            game = Game.objects.get(id=game_id)
            board = list(game.board)

            if board[position] == '-':  # Check if the position is empty
                board[position] = game.current_turn
                game.board = ''.join(board)

                # Check for winner
                lines = [
                    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                    (0, 4, 8), (2, 4, 6)  # Diagonals
                ]
                for line in lines:
                    if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != '-':
                        game.winner = game.current_turn
                        return Response({'message': 'You Won!'}, status=status.HTTP_200_OK)
                # Switch turns
                game.current_turn = 'O' if game.current_turn == 'X' else 'X'
                game.save()
                return Response({'message': 'Move successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid move. Position already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        except Game.DoesNotExist:
            return Response({'error': 'Game not found.'}, status=status.HTTP_404_NOT_FOUND)


class GameStateView(APIView):
    def get(self, request, game_id):
        try:
            game = Game.objects.get(id=game_id)
            return Response({'board': game.board, 'current_turn': game.current_turn, 'winner': game.winner},
                            status=status.HTTP_200_OK)
        except Game.DoesNotExist:
            return Response({'error': 'Game not found.'}, status=status.HTTP_404_NOT_FOUND)
