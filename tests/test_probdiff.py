from unittest import TestCase
import subprocess
from typing import List
from probdiff.probdiff import Case


class Test(TestCase):
    def test_main_example_1(self):
        self.assert_solve_cases(
            [
                "1 4 3 2",
                "4 5 5 5",
                "2 2 2 2"
            ],
            [2, 1, 0])

    def test_own_1(self):
        self.assert_solve([1, 1, 2, 2], 2)

    def test_main_own_1(self):
        self.assert_solve_cases(["1 1 2 2"], [2])

    def test_main_own_2(self):
        self.assert_solve_cases(["1 1 1 2 3 4"], [3])

    def test_main_own_3(self):
        self.assert_solve_cases(["2 3 4 1 1 1"], [3])

    def test_main_own_4(self):
        self.assert_solve_cases(["1 1 2 3 4 5 1 1"], [4])

    def test_main_own_5(self):
        self.assert_solve_cases(["1 2 3 3 2 1 1 2 3"], [4])

    def test_indices_by_occurrence_desc(self):
        def assert_indices_by_occurrence_desc(diffs: List[int], expected_indices: List[int]):
            self.assertEqual(Case(diffs)._indices_by_occurrence_desc(), expected_indices)

        assert_indices_by_occurrence_desc([1], [0])
        assert_indices_by_occurrence_desc([1, 2], [0, 1])
        assert_indices_by_occurrence_desc([1, 2, 1], [0, 2, 1])
        assert_indices_by_occurrence_desc([2, 1, 1], [1, 2, 0])

    def assert_solve(self, diffs: List[int], expected_result: int):
        result = Case(diffs).solve()
        self.assertEqual(expected_result, result)

    def assert_solve_cases(self, cases: List[str], expected_result: List[int]):
        result = self.run_problem_solver([str(len(cases))] + cases)
        self.assertEqual(expected_result, result)

    def run_problem_solver(self, lines: List[str]) -> List[int]:
        proc = subprocess.Popen(
            ['python', 'probdiff.py'],
            cwd='../probdiff',
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)

        self.write_input(proc, lines)

        proc.stdin.close()
        proc.wait()
        output = list(self.read_output(proc))
        proc.stdout.close()
        return output

    def write_input(self, proc, lines: List[str]):
        for line in lines:
            self.write_stdin_line(proc, line + '\n')

    def write_stdin_line(self, proc, line: str):
        proc.stdin.write(bytes(line, 'utf-8'))

    def read_output(self, proc) -> List[int]:
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            yield int(line)
