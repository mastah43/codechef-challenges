import sys
import math
from functools import reduce
from typing import List


class Case:
    def __init__(self, diffs: List[int]):
        self.diffs = diffs
        return


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def probdiff(diffs: List[int]) -> int:
    return 0


def read_input() -> List[Case]:
    test_case_count = int(sys.stdin.readline())
    print_err("test cases: " + str(test_case_count))
    cases: List[Case] = []
    for i in range(0, test_case_count):
        cases.append(read_input_test_case())
    return cases


def read_input_test_case() -> Case:
    diffs = [int(a) for a in sys.stdin.readline().split()]
    assert(len(diffs) > 0)
    return Case(diffs)


def main():
    cases = read_input()
    for case in cases:
        print(probdiff(case.diffs))


if __name__ == "__main__":
    main()
