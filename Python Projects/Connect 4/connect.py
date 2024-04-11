import random
import numpy as np
import random
import time
import matplotlib.pyplot as plt


# class Connect4:
#     def __init__(self):
#         self.board = [[0 for i in range(7)] for j in range(6)]
#         self.player = 1
#         self.winner = 0
#         self.last_move = None

#     def __str__(self):
#         s = ""
#         for i in range(6):
#             for j in range(7):
#                 s += str(self.board[i][j]) + " "
#             s += "\n"
#         return s

#     def play(self, col):
#         if self.winner != 0:
#             print("Game is over")
#             return
#         if col < 0 or col > 6:
#             print("Invalid column")
#             return
#         if self.board[0][col] != 0:
#             print("Column is full")
#             return
#         for i in range(5, -1, -1):
#             if self.board[i][col] == 0:
#                 self.board[i][col] = self.player
#                 break
#         self.check_winner()
#         if self.player == 1:
#             self.last_move = col
#             self.player = 2
#         else:
#             self.last_move = col
#             self.player = 1

#     def check_winner(self):
#         for i in range(6):
#             for j in range(7):
#                 if self.board[i][j] != 0:
#                     if self.check_horizontal(i, j) or self.check_vertical(i, j) or self.check_diagonal(i, j):
#                         self.winner = self.board[i][j]
#                         return

#     def check_horizontal(self, i, j):
#         if j > 3:
#             return False
#         for k in range(4):
#             if self.board[i][j + k] != self.board[i][j]:
#                 return False
#         return True

#     def check_vertical(self, i, j):
#         if i > 2:
#             return False
#         for k in range(4):
#             if self.board[i + k][j] != self.board[i][j]:
#                 return False
#         return True

#     def check_diagonal(self, i, j):
#         if i > 2 or j > 3:
#             return False
#         for k in range(4):
#             if self.board[i + k][j + k] != self.board[i][j]:
#                 return False
#         return True

#     def is_over(self):
#         return self.winner != 0

#     def get_winner(self):
#         return self.winner

# def play_game(bot1, bot2):
#     game = Connect4()

#     player = random.randint(1, 2)

#     while not game.is_over():
#         if player == 1:
#             game.play(bot1(game.board, game.player, game.last_move))
#         else:
#             game.play(bot2(game.board, game.player, game.last_move))
#         if game.is_over():
#             break
#         player = 3 - player
#         if 0 not in game.board[0]:
#             player = 0
#             break
#     return player   

class Connect4:
    def __init__(self):
        self.board = np.array([[0 for i in range(7)] for j in range(6)])
        self.player = 1
        self.winner = 0
        self.last_move = None

    def __str__(self):
        s = ""
        for i in range(6):
            for j in range(7):
                s += str(self.board[i][j]) + " "
            s += "\n"
        return s

    def play(self, col):
        # if self.winner != 0:
        #     print("Game is over")
        #     return
        if col < 0 or col > 6:
            print("Invalid column")
            return
        if self.board[0][col] != 0:
            print("Column is full")
            return
        for i in range(5, -1, -1):
            if self.board[i][col] == 0:
                self.board[i][col] = self.player
                break
        self.check_winner()
        if self.player == 1:
            self.last_move = col
            self.player = 2
        else:
            self.last_move = col
            self.player = 1

    def check_winner(self):
        for i in range(6):
            for j in range(7):
                if self.board[i][j] != 0:
                    if self.check_horizontal(i, j) or self.check_vertical(i, j) or self.check_diagonal(i, j):
                        self.winner = self.board[i][j]
                        return

    def check_horizontal(self, i, j):
        if j > 3:
            return False
        for k in range(4):
            if self.board[i][j + k] != self.board[i][j]:
                return False
        return True

    def check_vertical(self, i, j):
        if i > 2:
            return False
        for k in range(4):
            if self.board[i + k][j] != self.board[i][j]:
                return False
        return True

    def check_diagonal(self, i, j):
        if i > 2 or j > 3:
            return False
        for k in range(4):
            if self.board[i + k][j + k] != self.board[i][j]:
                return False
        return True

    def is_over(self):
        return self.winner != 0

    def get_winner(self):
        return self.winner

def play_game(bot1, bot2, print_game=False):
    game = Connect4()

    player = random.randint(1, 2)

    while not game.is_over():
        if print_game:
            print(game)
        if player == 1:
            game.play(bot1(game.board, game.player, game.last_move))
        else:
            game.play(bot2(game.board, game.player, game.last_move))
        if game.is_over():
            break
        player = 3 - player
        if 0 not in game.board[0]:
            player = 0
            break
    return player

def plot_board(board):
    # reduce size of image
    plt.figure(figsize=(3, 2))
    board = np.array(board)

    img = np.zeros((6, 7, 3))
    img[board == 1, 0] = 1
    img[board == 2, 2] = 1
    img[board == 0, :] = 1

    # plot the image
    plt.imshow(img)
    plt.show()

def visual_game(bot1, bot2):
    game = Connect4()

    player = random.randint(1, 2)
    print("Bot", player, "is red, and starts")
    print("Bot", 3-player, "is blue")

    while not game.is_over():
        if player == 1:
            game.play(bot1(game.board, game.player, game.last_move))
        else:
            game.play(bot2(game.board, game.player, game.last_move))
        if game.is_over():
            break
        player = 3 - player
        if 0 not in game.board[0]:
            player = 0
            break
        plot_board(game.board)
    plot_board(game.board)


def check_connect_four(board):
    def check_line(line):
        for i in range(len(line) - 3):
            if line[i] == line[i + 1] == line[i + 2] == line[i + 3] and line[i] != 0:
                return True
        return False

    def is_board_full():
        return all(cell != 0 for row in board for cell in row)

    def check_winner():
        # Check horizontal lines
        for row in board:
            if check_line(row):
                return True

        # Check vertical lines
        for col in range(len(board[0])):
            if check_line([board[row][col] for row in range(len(board))]):
                return True

        # Check diagonal lines (from top-left to bottom-right)
        for row in range(len(board) - 3):
            for col in range(len(board[0]) - 3):
                if check_line([board[row + i][col + i] for i in range(4)]):
                    return True

        # Check diagonal lines (from top-right to bottom-left)
        for row in range(3, len(board)):
            for col in range(len(board[0]) - 3):
                if check_line([board[row - i][col + i] for i in range(4)]):
                    return True

        return False
    if check_winner():
        return True
    
    else:
        return False
    
class Memory:
    def __init__(self, current):
        self.current = current


memory = Memory(0)
def tetris_bot(board, player, last_move):
    priority = [3, 4, 2, 1, 5, 6, 0]
    for i in range(len(priority)):
        if board[0][priority[i]] == 0:
            return priority[i]
        
def nokia(board, player, last_move):
    liste = [0,1,2,3,4,5,6,5,4,3,2,1]
    while True:
        if board[0][liste[memory.current]] == 0:
            a = memory.current
            memory.current+=1
            memory.current%=12
            return liste[a]
        else:
            memory.current+=1
            memory.current%=12
        
def moist_bot(board, player, last_move):
    a = random.randint(0,6)
    try:
        if board[0][last_move] == 0 and a<4:
            return last_move
        else:
            while True:
                a = random.randint(0,6)
                if board[0][a] == 0:
                    return a
    except:
        return random.randint(2,4)

def anish_giri(board, player, last_move):
    dict = {
    0:6,
    1:5,
    2:4,
    3:3,
    6:0,
    5:1,
    4:2
    }

    try:
        if board[0][dict[last_move]] == 0:
            return dict[last_move]
        else:
            while True:
                a = random.randint(0,6)
                if board[0][a] == 0:
                    return a
    except:
        while True:
            a = random.randint(0,6)
            if board[0][a] == 0:
                return a    


def zig(board, player, last_move):
    a = random.randint(-1,1)
    try:
        if board[0][last_move+a] == 0:
            if last_move+a == -1:
                return 6
            return last_move+a
        
        else:
            while True:
                a = random.randint(0,6)
                if board[0][a] == 0:
                    return a
    except:
        while True:
            a = random.randint(0,6)
            if board[0][a] == 0:
                return a





















# game.play(3)
# game.play(6)
# print(game.board)

# spill = Connect4()
# def morad(board, player, last_move):
#     spill = Connect4()
#     spill.board = board

#     dict = {}
#     for a in range(7):
#         dict[a]=0
#         brett = spill.board.copy()
#         brett.play(a)
#         if check_connect_four():
#             return a
        
#         for b in range(7):
#             brett.play(b)
#             if check_connect_four():
#                 return b

#             for c in range(7):
#                 brett.play(c)
#                 if check_connect_four():
#                     dict[a]+=1
                

#                 for d in range(7):
#                     brett.play(d)

#                     for e in range(7):
#                         brett.play(e)
#                         if check_connect_four():
#                             dict[a]+=1
                       

#                         for f in range(7):
#                             brett.play(f)

#                             for g in range(7):
#                                 brett.play(g)
#                                 if check_connect_four():
#                                     dict[a]+=1                             
#     return max(dict, key=lambda k: dict[k])






def morad(board, player, last_move):
    # print(player)
    spill = Connect4()
    spill.board = board.copy()
    spill.player = player
    
    # print(spill.board)
    original_board = board.copy()

    my_dict = {}
    for a in range(7):
        my_dict[a]=0
        spill.board = original_board.copy()
        spill.player = player
        # print(spill.player)
        if spill.board[0][a]==0:
            spill.play(a)
            if check_connect_four(spill.board):
                return a
        else:
            continue
        
        for b in range(7):
            if spill.board[0][b]==0:
                spill.play(b)
                if check_connect_four(spill.board):
                    return b   
            else:
                continue
            
            for c in range(7):
                if spill.board[0][c]==0:
                    spill.play(c)
                    if check_connect_four(spill.board):
                        my_dict[a]+=1
                else:
                    continue

            
                for d in range(7):
                    if spill.board[0][d]==0:
                        spill.play(d) 
                    else:
                        continue

                    for e in range(7):
                        if spill.board[0][e]==0:
                            spill.play(e)
                            if check_connect_four(spill.board):
                                my_dict[a]+=1
                        else:
                            continue

                        for f in range(7):
                            if spill.board[0][f]==0:
                                spill.play(f) 
                            else:
                                continue

                            for g in range(7):
                                if spill.board[0][g]==0:
                                    spill.play(g)
                                    if check_connect_four(spill.board):
                                        my_dict[a]+=1
                                else:
                                    continue
        
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    # print(sorted_dict)
    for key in sorted_dict:          
        if board[0][key]==0:          
            return key




# visual_game(morad, nokia)

N = 100
u = 0
for i in range(N):
    if play_game(morad, nokia)==1:
        u += 1
print("morad nokia")
print(u/N)

# N = 1000
# u = 0
# for i in range(N):
#     if play_game(anish_giri, moist_bot)==1:
#         u += 1
# print("tetris moist")
# print(u/N)

# N = 1000
# u = 0
# for i in range(N):
#     if play_game(anish_giri, tetris_bot)==1:
#         u += 1
# print("tetris tetris")
# print(u/N)


# N = 1000
# u = 0
# for i in range(N):
#     if play_game(anish_giri, zig)==1:
#         u += 1
# print("nokia zig")
# print(u/N)

# N = 1000
# u = 0
# for i in range(N):
#     if play_game(tetris_bot, zig)==1:
#         u += 1
# print("nokia zig")
# print(u/N)


# N = 1000
# u = 0
# for i in range(N):
#     if play_game(zig, moist_bot)==1:
#         u += 1
# print("zig moist")
# print(u/N)



# def plot_board(board):
#     # reduce size of image
#     plt.figure(figsize=(2, 3))
#     board = np.array(board)

#     img = np.zeros((6, 7, 3))
#     img[board == 1, 0] = 1
#     img[board == 2, 2] = 1
#     img[board == 0, :] = 1

#     # plot the image
#     plt.imshow(img)
#     plt.show()

# def visual_game(bot1, bot2):
#     game = Connect4()

#     player = random.randint(1, 2)

#     while not game.is_over():
#         if player == 1:
#             game.play(bot1(game.board, game.player, game.last_move))
#         else:
#             game.play(bot2(game.board, game.player, game.last_move))
#         if game.is_over():
#             break
#         player = 3 - player
#         if 0 not in game.board[0]:
#             player = 0
#             break
#         plot_board(game.board)
#     plot_board(game.board)
# visual_game(zig, morad)



#player 1 eller 2
#last move er tall



#øverste ikke er 0



    # if check_winner():
    #     return "Player 1 wins" if turn_count % 2 == 0 else "Player 2 wins"
    # elif is_board_full():
    #     return "Draw"
    # else:
    #     return "Game in progress"

# Example usage:








     

    


