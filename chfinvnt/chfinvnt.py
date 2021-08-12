import sys
from typing import List


class Case:
    def __init__(self, n: int, p: int, k: int):
        self.n = n
        self.p = p
        self.k = k
        return

    def solve(self):
        return self.n # TODO impl


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def read_input() -> List[Case]:
    test_case_count = int(sys.stdin.readline())
    cases: List[Case] = []
    for i in range(0, test_case_count):
        cases.append(read_input_test_case())
    return cases


def read_input_test_case() -> Case:
    n, p, k = [int(a) for a in sys.stdin.readline().split()]
    assert(len(n) > 1)
    assert(len(p) > 0)
    assert(len(p) <= n)
    assert(len(k) > 1)
    return Case(n, p, k)


def main():
    cases = read_input()
    for case in cases:
        print(case.solve())


if __name__ == "__main__":
    main()
