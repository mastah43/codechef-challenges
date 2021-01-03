import sys
from typing import List


class Game:
    def __init__(self, p1_score, p2_score):
        self.p1_score = p1_score
        self.p2_score = p2_score
        return


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def lead_game(games: List[Game]) -> (int, int):
    lead_game_cur = [0, 0]
    p1_score = 0
    p2_score = 0
    for game in games:
        p1_score += game.p1_score
        p2_score += game.p2_score
        lead_points = abs(p1_score - p2_score)
        if lead_points > lead_game_cur[1]:
            lead_player = 1 if (p1_score - p2_score) > 0 else 2
            lead_game_cur[0] = lead_player
            lead_game_cur[1] = lead_points
    return lead_game_cur


def read_input() -> List[Game]:
    games_count = int(sys.stdin.readline())
    games: List[Game] = []
    for i in range(0, games_count):
        games.append(read_input_game())
    return games


def read_input_game() -> Game:
    p1_score, p2_score = [int(x) for x in sys.stdin.readline().split()]
    return Game(p1_score, p2_score)


def main():
    games = read_input()
    lead_player, lead_score = lead_game(games)
    print(str(lead_player) + ' ' + str(lead_score))


if __name__ == "__main__":
    main()
