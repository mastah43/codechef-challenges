from unittest import TestCase
import subprocess
from typing import List
from arrfill.arrfill import Case, Move


class Test(TestCase):
    def test_solve_main_example_1(self):
        self.assert_solve_lines(
            [
                "3",
                "10 1",
                "5 2",
                "8 2",
                "5 2",
                "6 3",
                "3 2",
                "2 2",
                "1 3"
            ],
            [25, 41, 5])

    def test_solve_example_1_1(self):
        self.assert_solve(Case(10, [Move(5, 2)]), 25)

    def test_solve_example_1_2(self):
        self.assert_solve(Case(8, [Move(5, 2), Move(6, 3)]), 41)

    def test_solve_example_1_3(self):
        self.assert_solve(Case(3, [Move(2, 2), Move(1, 3)]), 5)

    def assert_solve(self, case: Case, max_sum_expected: int):
        max_sum = case.solve()
        self.assertEqual(max_sum_expected, max_sum)

    def assert_solve_lines(self, lines: List[str], expected_result: List[int]):
        result = self.run_problem_solver(lines)
        self.assertEqual(expected_result, result)

    def run_problem_solver(self, lines: List[str]) -> List[int]:
        proc = subprocess.Popen(
            ['python', 'arrfill.py'],
            cwd='../arrfill',
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
