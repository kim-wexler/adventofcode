import sys

data = sys.stdin.read()
data = [line.split(" ") for line in data.strip().split("\n")]

# X = lose, Y = draw, Z = win
# A/X = rock, B/Y = paper, C/Z = scissors
scores = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}
choose_loser = {"A": "C", "B": "A", "C": "B"}
choose_winner = {"A": "B", "B": "C", "C": "A"}

def pt1(opponent, player):
    if ord(player) - 23 == ord(choose_winner[opponent]):
        return 6 + scores[player]
    elif ord(player) - 23 == ord(opponent):
        return 3 + scores[player]
    else:
        return scores[player]

def pt2(opponent, player):
    if player == "X":
        return scores[choose_loser[opponent]]
    elif player == "Y":
        return 3 + scores[opponent]
    else:
        return 6 + scores[choose_winner[opponent]]


ans = sum([pt1(game[0], game[1]) for game in data])
ans2 = sum([pt2(game[0], game[1]) for game in data])
print(ans, ans2)
