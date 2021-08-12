import sys
import math
from functools import reduce
from typing import List


class Case:
    def __init__(self, diffs: List[int]):
        self.diffs = diffs
        self.sets = [0 for i in range(len(self.diffs))]
        return

    def _is_addable_to_set(self, set_id: int, diff: int):
        set_size = 0
        for i in range(len(self.sets)):
            if self.sets[i] == set_id:
                set_size += 1
                if set_size >= 2 or (self.diffs[i] == diff):
                    return False
        return True

    def _count_complete_sets(self):
        counts_by_set_id = dict()
        for i in range(len(self.sets)):
            set_id = self.sets[i]
            counts_by_set_id.setdefault(set_id, 0)
            counts_by_set_id[set_id] += 1

        return sum(map(lambda set_size: 1 if set_size >= 2 else 0, counts_by_set_id.values()))

    def solve(self) -> int:
        self.sets = [0 for i in range(len(self.diffs))]
        current_set_id = 1
        for i in range(len(self.diffs)):
            diff = self.diffs[i]
            set_id = 1
            while not self._is_addable_to_set(set_id=set_id, diff=diff):
                set_id += 1
            self.sets[i] = set_id

        return self._count_complete_sets()


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


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
        print(case.solve())


if __name__ == "__main__":
    main()
