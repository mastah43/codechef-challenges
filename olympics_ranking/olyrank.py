import sys
import math
from functools import reduce
from typing import List


class Medals:
    def __init__(self, country: int, g: int, s: int, b: int):
        self.country = country
        self.g = g
        self.s = s
        self.b = b
        return

    def count_medals(self):
        return self.g+self.s+self.b


class Case:
    def __init__(self, m1: Medals, m2: Medals):
        self.m1 = m1
        self.m2 = m2
        return


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def olyrank(medals1: Medals, medals2: Medals) -> int:
    return medals1.country if medals1.count_medals() > medals2.count_medals() else medals2.country


def read_input() -> List[Case]:
    test_case_count = int(sys.stdin.readline())
    cases: List[Case] = []
    for i in range(0, test_case_count):
        cases.append(read_input_test_case())
    return cases


def read_input_test_case() -> Case:
    g1, s1, b1, g2, s2, b2 = [int(x) for x in sys.stdin.readline().split()]
    return Case(Medals(1, g1, s1, b1), Medals(2, g2, s2, g2))


def main():
    cases = read_input()
    for case in cases:
        print(str(olyrank(case.m1, case.m2)))


if __name__ == "__main__":
    main()
