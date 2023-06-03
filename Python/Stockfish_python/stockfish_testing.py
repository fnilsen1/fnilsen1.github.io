
colorOfPlayer = 'White'

dict = {
    "rnbqkb1r/1p2pppp/p4n2/3p4/3P1B2/2N2N2/PP2PPPP/R2QKB1R b KQkq - 1 6": {
        "count": 6,
        "eval": 39,
        "links": [
            "https://lichess.org/mvHBzvSE",
            "https://lichess.org/Lkl2cLdz",
            "https://lichess.org/DCtgAXqt",
            "https://lichess.org/mMiUUWNQ",
            "https://lichess.org/meXSO0NR",
            "https://lichess.org/UoVqZlQV"
        ]
    },
    "rnbq1rk1/pp2bppp/2p1pn2/3p2B1/2PP4/2NBPN2/PP3PPP/R2QK2R b KQ - 2 7": {
        "count": 6,
        "eval": 41,
        "links": [
            "https://lichess.org/yrtv5Lkd",
            "https://lichess.org/SzVQ1mEg",
            "https://lichess.org/LM231Vjs",
            "https://lichess.org/DlQYTfNg",
            "https://lichess.org/HbbsKHoX",
            "https://lichess.org/52zukd3f"
        ]
    },
    "r1bqk2r/pp1n1ppp/2pbpn2/3p4/2PP4/2NBPN2/PP3PPP/R1BQ1RK1 b kq - 4 7": {
        "count": 6,
        "eval": 45,
        "links": [
            "https://lichess.org/ZNtMSWcP",
            "https://lichess.org/zSRMG7nB",
            "https://lichess.org/jU2XDG9v",
            "https://lichess.org/6zWejzrG",
            "https://lichess.org/amYTp2TC",
            "https://lichess.org/jIpokfPR"
        ]
    }}

sorted_dict = {k: v for k, v in sorted(dict.items(), key=lambda item: (-item[1]['count'], item[1]['eval'] if colorOfPlayer == 'White' else -item[1]['eval']))}
print(sorted_dict)