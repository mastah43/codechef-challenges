import sys
from typing import List


class Case:
    def __init__(self, d, ages):
        self.d = d
        self.ages = ages
        return


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def is_risk_age(age) -> bool:
    return age <= 9 or age >= 80


def days_to_vaccine_distributed(people_per_day: int, ages: List[int]) -> int:
    return 0


def read_input() -> List[Case]:
    test_case_count = int(sys.stdin.readline())
    print_err("test cases: " + str(test_case_count))
    cases: List[Case] = []
    for i in range(0, test_case_count):
        cases.append(read_input_test_case())
    return cases


def read_input_test_case() -> Case:
    n, d = [int(x) for x in sys.stdin.readline().split()]
    ages = [int(a) for a in sys.stdin.readline().split()]
    assert(len(ages) == n)
    return Case(d, ages)


def main():
    cases = read_input()
    for case in cases:
        print(days_to_vaccine_distributed(case.d, case.ages))


if __name__ == "__main__":
    main()
