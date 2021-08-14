import sys
from typing import List
from itertools import permutations

class Move:
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
        max_array_sum = -1
        best_moves = list()
        for moves in permutations(self.moves):
            self._reset_array()
            self._apply_moves(moves)
            array_sum = self._array_sum()
            if array_sum > max_array_sum:
                max_array_sum = array_sum
                best_moves = moves
        return max_array_sum

    def _reset_array(self):
        self.a = [0 for i in range(len(self.a))]

    def _apply_moves(self, moves):
        for move in moves:
            self._apply_move(move)

    def _apply_move(self, move):
        for i, aj in enumerate(self.a):
            j = i + 1
            if aj == 0 and j % move.y != 0:
                self.a[i] = move.x

    def _array_sum(self):
        return sum(self.a)


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
