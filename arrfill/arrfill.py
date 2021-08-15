import sys
from typing import List
from itertools import permutations

class Move:
    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        return


class Case:
    def __init__(self, n: int, moves: List[Move]):
        self.a = [0 for i in range(n)]
        self.moves = moves
        return

    def solve(self):
        self._reset_array()
        best_moves = list()
        moves_ordered = self._sorted_moves_by_value()
        print_err("moves ordered: " + str(moves_ordered))
        while len(moves_ordered) > 0:
            move_chosen_i = -1
            sum_inc_max = -1
            for i, move in enumerate(moves_ordered):
                sum_inc = self._get_sum_increment_by_move(move)
                if sum_inc > sum_inc_max:
                    sum_inc_max = sum_inc
                    move_chosen_i = i

            move_chosen = moves_ordered.pop(move_chosen_i)
            print_err("move chosen: " + str(move_chosen))
            best_moves.append(move_chosen)
            self._apply_move(move_chosen)

        print_err("best moves: " + str(best_moves))

        return self._array_sum()

    def _sorted_moves_by_value(self):
        return sorted(self.moves,
                      key=lambda move: move.x,
                      reverse=True)

    def _reset_array(self):
        self.a = [0 for i in range(len(self.a))]

    def _apply_moves(self, moves):
        for move in moves:
            self._apply_move(move)

    def _apply_move(self, move):
        for i, ai in enumerate(self.a):
            if self._is_move_applicable_to_index(ai, i, move):
                self.a[i] = move.x

    def _is_move_applicable_to_index(self, ai, i, move):
        return ai == 0 and (i + 1) % move.y != 0

    def _array_sum(self):
        return sum(self.a)

    def _get_sum_increment_by_move(self, move):
        sum_inc = 0
        for i, ai in enumerate(self.a):
            if self._is_move_applicable_to_index(ai, i, move):
                sum_inc += move.y
        return sum_inc


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
