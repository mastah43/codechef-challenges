import sys
import math
from functools import reduce
from typing import List


class Case:
    def __init__(self, d, ages):
        self.d = d
        self.ages = ages
        return


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def is_risk_age(age: int) -> bool:
    return age <= 9 or age >= 80


def is_no_risk_age(age: int) -> bool:
    return not is_risk_age(age)


def days_to_vaccine_distributed(people_per_day: int, ages: List[int]) -> int:
    count_people_risk = sum(1 for age in filter(is_risk_age, ages))
    count_people_no_risk = len(ages) - count_people_risk
    return math.ceil(count_people_risk / people_per_day) + math.ceil(count_people_no_risk / people_per_day)


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
