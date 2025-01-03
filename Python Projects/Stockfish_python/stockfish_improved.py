import chess
import chess.engine
import json
import re

colorOfPlayer = 'White'
pgnFile = "PGNs\Hako2005-white.pgn"

fileName = "Hakon_hvit_analyse"
urls = []
games = []

def returnFromPGN():
    regexURL = r'\[Site "(.*?)"]'
    regexGame = r'\[Termination[\s\S]*?\][\s\S]*?(.*?)(1-0|0-1|1\/2-1\/2)'

    with open(pgnFile, 'r',encoding="utf8") as f:
        text = f.read()

    urlMatches = re.findall(regexURL, text)
    gameMatches = re.findall(regexGame, text)

    for match in urlMatches:
        urls.append(match)

    for match in gameMatches:
        games.append(list(filter(lambda x: '.' not in x and x != '', match[0].split(' '))))

returnFromPGN()

engine = chess.engine.SimpleEngine.popen_uci("stockfish-windows-x86-64-avx2.exe")
def stockfish_evaluation(board, time_limit = 0.01):

    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    return result['score']

dict = {
}

for i in range(len(games)):
    board = chess.Board()
    for j in range(len(games[i])):
        board.push_san(games[i][j])
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

# sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1]['count'], item[1]['eval'] if colorOfPlayer != 'White' else -item[1]['eval']))}
sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1]['count'], item[1]['eval'] if colorOfPlayer == 'White' else -item[1]['eval']))}

# sorted_dict1 = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1]['count'], reverse=True)}
# sorted_dict = {k: v for k, v in sorted(sorted_dict1.items(), key=lambda item: item[1]['eval'], reverse=(colorOfPlayer != 'White'))}

filnavn = "håkon_test"+".json"
with open(filnavn, "w") as fil:
    fil.write(json.dumps(sorted_dict, indent = 4))
print("Ferdig!")

