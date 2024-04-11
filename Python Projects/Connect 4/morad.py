import copy

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

def morad(board, player, last_move):
    if last_move == None:
        return 3

    spill = Connect4()
    spill.board = copy.deepcopy(board)
    spill.player = player
    original_board = copy.deepcopy(board)

    my_dict = {}


    for a in range(7):
        my_dict[a]=0
        spill.board = copy.deepcopy(original_board)
        spill.player = player

        if spill.board[0][a]==0:
            
            spill.play(a)

            save = copy.deepcopy(spill.board)
            if check_connect_four(spill.board):
                return a

        else:
            continue
        
        for b in range(7):
            # print(save)
            spill.board = copy.deepcopy(save)
            
            spill.player = 3-player

            if spill.board[0][b]==0:
                spill.play(b)

                save1 = copy.deepcopy(spill.board)
                if check_connect_four(spill.board) and a!=b:
                    return b


    for a in range(7):
        my_dict[a]=0
        spill.board = copy.deepcopy(original_board)
        spill.player = player

        if spill.board[0][a]==0:
            
            spill.play(a)

            save = copy.deepcopy(spill.board)

        else:
            continue
        
        for b in range(7):
            # print(save)
            spill.board = copy.deepcopy(save)
            
            spill.player = 3-player

            if spill.board[0][b]==0:
                spill.play(b)

                save1 = copy.deepcopy(spill.board)

            else:
                continue
            
            for c in range(7):
                spill.board = copy.deepcopy(save1)
                spill.player = player

                if spill.board[0][c]==0:
                    spill.play(c)
                    save2 = copy.deepcopy(spill.board)

                    if check_connect_four(spill.board):
                        my_dict[a]+=1
                        continue
                else:
                    continue

            
                for d in range(7):
                    spill.board = copy.deepcopy(save2)
                    spill.player = 3-player

                    if spill.board[0][d]==0:
                        spill.play(d) 
                        save3 = copy.deepcopy(spill.board)
                        if check_connect_four(spill.board):
                            my_dict[a]-=1
                            continue

                    else:
                        continue

                    for e in range(7):
                        spill.board = copy.deepcopy(save3)
                        spill.player = player

                        if spill.board[0][e]==0:
                            spill.play(e)
                            save4 = copy.deepcopy(spill.board)


                            if check_connect_four(spill.board):
                                my_dict[a]+=1
                                continue
                        else:
                            continue

                        for f in range(7):
                            spill.board = copy.deepcopy(save4)
                            spill.player = 3-player


                            if spill.board[0][f]==0:
                                spill.play(f) 
                                save5 = copy.deepcopy(spill.board)


                                if check_connect_four(spill.board):
                                    my_dict[a]-=1
                                    continue
                            else:
                                continue

                            for g in range(7):
                                spill.board = copy.deepcopy(save5)
                                spill.player = player


                                if spill.board[0][g]==0:
                                    spill.play(g)
                                    if check_connect_four(spill.board):
                                        my_dict[a]+=1
                                        continue
                                else:
                                    continue
        
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    for key in sorted_dict:          
        if board[0][key]==0:          
            return key
        