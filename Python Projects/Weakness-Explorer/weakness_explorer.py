import chess
import chess.engine
import json
import re
"""
How to use:
Put your pgn in the "PGNs" folder
Change the 3 lines below
Open the result in the "out" folder
"""

#Change these 3 lines
colorOfPlayer = 'White'
pgnFile = r"PGNs\vetles05-white.pgn"
fileName = "vetle_hvit_analyse"
#no error handling cuz fuck u, just do it correctly

urls = []
games = []

def analyse(pgnFile, colorOfPlayer):
        urls = []
        games = []

        def returnFromPGN():
            with open(pgnFile, 'r', encoding="utf8") as f:
                text = f.read()

            regexURL = r'\[Site "(.*?)"]'
            urlMatches = re.findall(regexURL, text)
            website = urlMatches[0].replace('https://', '').split('.')[0]
            if (website == "Chess"):
                urlMatches.clear()
                urlMatches = re.findall(r'\[Link "(.*?)"]', text)
            regexGame = r'\[Termination[\s\S]*?\][\s\S]*?(.*?)(1-0|0-1|1\/2-1\/2)' if website == 'lichess' else r'\[Link[\s\S]*?\][\s\S]*?(.*?)(1-0|0-1|1\/2-1\/2)'
            gameMatches = re.findall(regexGame, text)

            for match in urlMatches:
                urls.append(match)

            for match in gameMatches:
                games.append(list(filter(lambda x: '.' not in x and x != '', match[0].split(' '))))
            
        returnFromPGN()

        engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-2022-x86-64-avx2.exe")
        def stockfish_evaluation(board, time_limit = 0.01):

            result = engine.analyse(board, chess.engine.Limit(time=time_limit))
            return result['score']

        dict = {}

        gameN = 0
        for i in range(len(games)):
            break_outer_loop = False
            gameN += 1
            print(str(gameN) + " / " + str(len(games)))
            board = chess.Board()
            for j in range(len(games[i])):
                try:
                    board.push_san(games[i][j])
                except:
                    break_outer_loop = True
                    break
                # board.push_san(games[i][j])
                fen = board.fen()

                modn = 0 if colorOfPlayer == 'White' else 1
                if(j % 2 == modn and j > 7):
                    if (fen not in dict):
                        dict[fen] = {}
                        dict[fen]["count"] = 0
                        dict[fen]["eval"] = 0
                        dict[fen]["links"] = []
                    
                    s=str(stockfish_evaluation(board))
                    regex = r"^\w+\((\w+)\(([\+\-]?\d+)\),\s*(\w+)\)$"

                    match = re.search(regex, s)
                    mate = match.group(1) == 'Mate'
                    evalN = int(match.group(2))
                    col = match.group(3)
                    number = evalN
                    
                    if (mate):
                        if (evalN == 0):
                            number = 0
                        else:
                            number = 100000 * (evalN / abs(evalN)) - ((abs(evalN) - 1) * (evalN / abs(evalN))) * 1000
                    
                    number = int(number) if col == 'WHITE' else -int(number)

                    dict[fen]["eval"] = number
                    dict[fen]["links"].append(urls[i])
                    dict[fen]["count"] += 1
            if break_outer_loop:
                continue

        sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1]['count'], item[1]['eval'] if colorOfPlayer == 'White' else -item[1]['eval']))}

        # custom = pgnFile.split(".")[-2].split("/")[-1]

        filnavn = "out/"+fileName+".json"
        with open(filnavn, "w") as fil:
            fil.write(json.dumps(sorted_dict, indent = 4))
        fil.close()
        print("Done!")

analyse(pgnFile, colorOfPlayer)
