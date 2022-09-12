import sys
from typing import List
import math

class Move:
    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        return


class Case:
    def __init__(self, n: int, moves: List[Move]):
        self.n = n
        self.moves = moves
        return

    def solve(self):
        best_moves = list()
        moves_ordered = self._sorted_moves_by_value()
        print_err("moves ordered: " + str(moves_ordered))
        while len(moves_ordered) > 0:
            #move_chosen_i = -1
            #sum_inc_max = -1
            for i, move in enumerate(moves_ordered):
                #sum_inc = self._get_sum_increment_by_move(best_moves, move)
                #if sum_inc > sum_inc_max:
                #    sum_inc_max = sum_inc
                #    move_chosen_i = i

                move_chosen_i = i
                move_chosen = moves_ordered.pop(move_chosen_i)
                print_err("move chosen: " + str(move_chosen))
                best_moves.append(move_chosen)

        print_err("best moves: " + str(best_moves))
        return self._array_sum(best_moves)

    def _sorted_moves_by_value(self):
        return sorted(self.moves,
                      key=lambda move: move.x,
                      reverse=True)

    def _array_sum(self, moves: List[Move]):
        arr_sum = 0
        moves_before = List[Move]()
        for move in moves:
            arr_sum += self._get_sum_increment_by_move(moves_before, move)
        return arr_sum

    def _get_sum_increment_by_move(self, moves_before, move):
        indices_taken_before = 0
        for move_before in moves_before:
            indices_taken_cur = self.n // move_before.y
            lcm = Case._lcm(move.x, moves_before.x)
            indices_taken_by_move_before = self.n // lcm
            # TODO how to determine overlap with e.g. move before 1 and move before 2 but not counting the overlap between move before 1 & 2
            indices_taken_before += indices_taken_cur

        indices_new_move = max(0, self.n // move.y - indices_taken_before)
        return indices_new_move * move.y

    @staticmethod
    def _lcm(a, b):
        return abs(a * b) // math.gcd(a, b)


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def read_input() -> List[Case]:
    test_case_count = int(sys.stdin.readline())
    cases: List[Case] = []
    for i in range(0, test_case_count):
        cases.append(read_input_test_case())
    return cases


def read_input_test_case() -> Case:
    n, m = [int(a) for a in sys.stdin.readline().split()]
    assert (n >= 1)
    assert (m >= 1)

    moves = list[Move]()
    for i in range(m):
        x, y = [int(a) for a in sys.stdin.readline().split()]
        assert(x >= 1)
        assert(y >= 2)
        assert(y <= n)
        moves.append(Move(x, y))

    return Case(n, moves)


def main():
    cases = read_input()
    for case in cases:
        print(case.solve())


if __name__ == "__main__":
    main()
