# we want to code connect4
import numpy as np
import random
import time
import matplotlib.pyplot as plt
from numba import njit


def plot_board(board):
    plt.figure(figsize=(2.5, 2.5))
    board = np.array(board)  # Assuming self.board is the attribute containing your board data

    for i in range(6):
        for j in range(7):
            x = j
            y = 6-i
            if board[i][j] == 1:
                plt.plot(x, y, 'o', color='green', markersize=14)
            elif board[i][j] == 2:
                plt.plot(x, y, 'o', color='red', markersize=14)
    # change so we plot a bit more in each direction
    plt.xlim(-0.5, 6.5)
    plt.ylim(0.5, 6.5)

    # set background to dark gray
    ax = plt.gca()
    ax.set_facecolor((1, 1, 1))

    # remove the ticks and axis labels
    plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
    
    plt.show()


class Connect4:
    def __init__(self):
        self.board = np.array([[0 for i in range(7)] for j in range(6)])
        self.player = 1
        self.winner = 0
        self.moves_made = []

    def __str__(self):
        s = ""
        for i in range(6):
            for j in range(7):
                s += str(self.board[i][j]) + " "
            s += "\n"
        return s

    def switch_player(self):
        self.player = 3 - self.player

    def play(self, move): # we will use a function to play the game,
        if self.board[0][move] != 0:
            print("Invalid move")
            return False
        for i in range(5, -1, -1):
            if self.board[i][move] == 0:
                self.board[i][move] = self.player
                break
        self.moves_made.append(move)
        self.switch_player()
        return True

    def plot(self):
        plot_board(self.board)


@njit
def check_winner(board):
    # returns 0 if no winner, 1 if player 1 won, 2 if player 2 won

    # check horizontal
    for i in range(6):
        for j in range(4):
            if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i][j + 2] and board[i][j] == board[i][j + 3]:
                return board[i][j]

    # check vertical
    for i in range(3):
        for j in range(7):
            if board[i][j] != 0 and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 2][j] and board[i][j] == board[i + 3][j]:
                return board[i][j]

    # check diagonal
    for i in range(3):
        for j in range(4):
            if board[i][j] != 0 and board[i][j] == board[i + 1][j + 1] and board[i][j] == board[i + 2][j + 2] and board[i][j] == board[i + 3][j + 3]:
                return board[i][j]

    # check other diagonal
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] != 0 and board[i][j] == board[i + 1][j - 1] and board[i][j] == board[i + 2][j - 2] and board[i][j] == board[i + 3][j - 3]:
                return board[i][j]

    return 0


def play_game(bot1, bot2, start_player = 0, visualize = False, print_moves = False, halt = False):
    if start_player == 0:
        start_player = random.randint(1, 2)
    
    game = Connect4()
    game.player = start_player
    winner = 0

    while True:
        botname = bot1.__name__ if game.player == 1 else bot2.__name__
        if game.player == 1:
            move = bot1(game.board, game.player, game.moves_made[-1] if len(game.moves_made) > 0 else None)
        else:
            move = bot2(game.board, game.player, game.moves_made[-1] if len(game.moves_made) > 0 else None)
        flag = game.play(move)
        if flag == False:
            winner = 3 - game.player
            print(f"{botname} ({3-game.player}) made an invalid move, and therefore loses")
            return winner, start_player, game.moves_made

        if print_moves:
            print(f"{botname} ({3-game.player}) played {move}")

        if visualize == "print":
            print(game)
        if visualize == "plot":
            game.plot()

        winner = check_winner(game.board)
        if winner != 0:
            break
        if 0 not in game.board[0]:
            winner = 0
            break

        if halt:
            inp = input("Press enter to continue, type 'q' to quit")
            if inp == "q":
                break

    # print the name of the bot (function name)
    if print_moves:
        if winner == 1:
            print("The winner is",bot1.__name__)
        elif winner == 2:
            print("The winner is",bot2.__name__)
        else:
            print("It's a draw")

    return winner, start_player, game.moves_made


def playback_game(moves_made, start_player, halt = False):
    game = Connect4()
    game.player = start_player
    for move in moves_made:
        game.play(move)
        game.plot()
        print(game)
        if halt:
            inp = input("Press enter to continue, type 'q' to quit")
            if inp == "q":
                break


def human_bot(board, player, last_move):
    while True:
        move = int(input(f"Last move done was {last_move}. \nhuman_bot({player}), enter your move: "))
        if board[0][move] == 0:
            return move
        else:
            print("Invalid move")


def simulate_games(bot1, bot2, N = 100, start_player = 0):
    # simulates N games between bot1 and bot2
    # returns the number of games won by bot1 and bot2

    bot1_wins = 0
    bot2_wins = 0
    draws = 0
    games = []

    for i in range(N):
        winner, start_player, moves_made = play_game(bot1, bot2, start_player = start_player)
        games.append([winner, start_player, moves_made])
        if winner == 1:
            bot1_wins += 1
        elif winner == 2:
            bot2_wins += 1
        else:
            draws += 1

    return bot1_wins, bot2_wins, draws, games


# # example of how to play a game:
# # here we play a game between two humans, after each move the move made (0-6) is printed and the board is plotted
# play_game(human_bot, human_bot, visualize = "plot", print_moves = True, halt = False)
