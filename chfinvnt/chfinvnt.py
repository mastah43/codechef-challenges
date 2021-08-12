import sys
from typing import List


class Case:
    def __init__(self, n: int, p: int, k: int):
        self.n = n
        self.p = p
        self.k = k
        return

    def solve(self):
        n_k_remainder = self.n % self.k
        n_k_div = self.n // self.k
        full_iterations = self.p % self.k
        days_full_iterations = full_iterations * n_k_div + min(n_k_remainder, full_iterations)
        days_after_full_iterations = self.p // self.k + 1
        days = days_full_iterations + days_after_full_iterations
        return days


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
    assert(n >= 1)
    assert(p >= 0)
    assert(p <= n)
    assert(k >= 1)
    return Case(n, p, k)


def main():
    cases = read_input()
    for case in cases:
        print(case.solve())


if __name__ == "__main__":
    main()
