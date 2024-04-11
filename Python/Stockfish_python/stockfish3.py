import chess
import chess.engine
import json
import re


FEN = "qrb5/rk1p1K2/p2P4/Pp6/1N2n3/6p1/5nB1/6b1 w - - 0 1"
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\filip\OneDrive - NTNU\Desktop\GitHub\fnilsen1.github.io\Python\Stockfish_python\stockfish-windows-x86-64-avx2.exe")
def stockfish_evaluation(board, time_limit = 10):

    result = engine.analyse(board, chess.engine.Limit(depth=30), multipv=3)

    liste = []
    # print(result)
    for i in range(3):
        streng = ""
        board = chess.Board(FEN)
        for move in result[i]["pv"]:
            uci_move = str(move)
            move_obj = chess.Move.from_uci(uci_move)
            algebraic_notation = board.san(move_obj)
            streng += algebraic_notation + " "

            # Apply the move to the board
            board.push(move_obj)
        liste.append(streng.strip())

    return liste
board = chess.Board(FEN)
print(stockfish_evaluation(board))



# import chess
# import chess.engine
# import smtplib
# import ssl
# from email.message import EmailMessage


# engine = chess.engine.SimpleEngine.popen_uci("/home/filipok04/ChessRaspberry/stockfish")
# def stockfish_evaluation(board, time_limit = 18):
#     result = engine.analyse(board, chess.engine.Limit(time=time_limit), multipv=3)

#     liste = []
#     # print(result)
#     for i in range(3):
#         streng = ""
#         board = chess.Board(fen)
#         for move in result[i]["pv"]:
#             uci_move = str(move)
#             move_obj = chess.Move.from_uci(uci_move)
#             algebraic_notation = board.san(move_obj)
#             streng += algebraic_notation + " "

#             # Apply the move to the board
#             board.push(move_obj)
#         liste.append(streng.strip())

#     return (liste, result)

# fen = input("FEN: ")
# board = chess.Board(fen)
# print(stockfish_evaluation(board))


# pgnFile = r'Python\Stockfish_python\PGNs\tobiasgnilsen99-black.pgn'
# fileName = "Tobias_analyse_black"
# urls = []
# games = []

# def analyse(pgnFile, colorOfPlayer):
#         urls = []
#         games = []

#         def returnFromPGN():
#             with open(pgnFile, 'r', encoding="utf8") as f:
#                 text = f.read()

#             regexURL = r'\[Site "(.*?)"]'
#             urlMatches = re.findall(regexURL, text)
#             website = urlMatches[0].replace('https://', '').split('.')[0]
#             if (website == "Chess"):
#                 urlMatches.clear()
#                 urlMatches = re.findall(r'\[Link "(.*?)"]', text)
#             regexGame = r'\[Termination[\s\S]*?\][\s\S]*?(.*?)(1-0|0-1|1\/2-1\/2)' if website == 'lichess' else r'\[Link[\s\S]*?\][\s\S]*?(.*?)(1-0|0-1|1\/2-1\/2)'
#             gameMatches = re.findall(regexGame, text)

#             for match in urlMatches:
#                 urls.append(match)

#             for match in gameMatches:
#                 games.append(list(filter(lambda x: '.' not in x and x != '', match[0].split(' '))))
            
#         returnFromPGN()

#         engine = chess.engine.SimpleEngine.popen_uci("Python\Stockfish_python\stockfish-windows-2022-x86-64-avx2.exe")
#         def stockfish_evaluation(board, time_limit = 0.01):

#             result = engine.analyse(board, chess.engine.Limit(time=time_limit))
#             return result['score']

#         dict = {}

#         gameN = 0
#         for i in range(len(games)):
#             break_outer_loop = False
#             gameN += 1
#             print(str(gameN) + " / " + str(len(games)))
#             board = chess.Board()
#             for j in range(len(games[i])):
#                 try:
#                     board.push_san(games[i][j])
#                 except:
#                     break_outer_loop = True
#                     break
#                 # board.push_san(games[i][j])
#                 fen = board.fen()

#                 modn = 0 if colorOfPlayer == 'White' else 1
#                 if(j % 2 == modn and j > 7):
#                     if (fen not in dict):
#                         dict[fen] = {}
#                         dict[fen]["count"] = 0
#                         dict[fen]["eval"] = 0
#                         dict[fen]["links"] = []
                  
                    
#                     s=str(stockfish_evaluation(board))
#                     regex = r"^\w+\((\w+)\(([\+\-]?\d+)\),\s*(\w+)\)$"

#                     match = re.search(regex, s)
#                     mate = match.group(1) == 'Mate'
#                     evalN = int(match.group(2))
#                     col = match.group(3)
#                     number = evalN
                    
#                     if (mate):
#                         number = 0
#                         """ if (evalN == 0):
#                             number = 0
#                         else:
#                             number = 100000 * (evalN / abs(evalN)) - ((abs(evalN) - 1) * (evalN / abs(evalN))) * 1000 """
                    
#                     number = int(number) if col == 'WHITE' else -int(number)

#                     dict[fen]["eval"] = number
#                     dict[fen]["links"].append(urls[i])
#                     dict[fen]["count"] += 1
                  
#             if break_outer_loop:
#                 continue

#         # sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1]['count'], item[1]['eval'] if colorOfPlayer == 'White' else -item[1]['eval']))}
#         sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1]['count'], item[1]['eval'] if colorOfPlayer == 'White' else -item[1]['eval']))}

#         # custom = pgnFile.split(".")[-2].split("/")[-1]
#         filnavn = "Python\Stockfish_python\out\\"+fileName+".json"
#         with open(filnavn, "w") as fil:
#             fil.write(json.dumps(sorted_dict, indent = 4))
#         print("Ferdig!")



# analyse(pgnFile, colorOfPlayer)