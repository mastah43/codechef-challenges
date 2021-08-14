import sys
from typing import List

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
        from itertools import permutations
        return 0


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
