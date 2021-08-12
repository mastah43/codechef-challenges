from unittest import TestCase
import subprocess
from typing import List
from chfinvnt.chfinvnt import Case


class Test(TestCase):
    def test_solve_main_example_1(self):
        self.assert_solve_cases(
            [
                "10 5 5",
                "10 6 5",
                "10 4 5",
                "10 8 5"
            ],
            [2, 4, 9, 8])

    def test_solve_example_1_1(self):
        self.assert_solve(10, 5, 5, 2)

    def test_solve_example_1_2(self):
        self.assert_solve(10, 6, 5, 4)

    def test_solve_example_1_3(self):
        self.assert_solve(10, 4, 5, 9)

    def test_solve_example_1_4(self):
        self.assert_solve(10, 8, 5, 8)

    def test_solve_simplest(self):
        self.assert_solve(1, 0, 1, 1)

    def test_solve_two_a(self):
        self.assert_solve(2, 1, 1, 2)

    def test_solve_two_b(self):
        self.assert_solve(2, 1, 2, 2)

    def test_solve_three_a(self):
        self.assert_solve(3, 1, 2, 3)

    def assert_solve(self, n:int, p:int, k:int, expected_days: int):
        days = Case(n, p, k).solve()
        self.assertEqual(expected_days, days)

    def assert_solve_cases(self, cases: List[str], expected_result: List[int]):
        result = self.run_problem_solver([str(len(cases))] + cases)
        self.assertEqual(expected_result, result)

    def run_problem_solver(self, lines: List[str]) -> List[int]:
        proc = subprocess.Popen(
            ['python', 'chfinvnt.py'],
            cwd='../chfinvnt',
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
