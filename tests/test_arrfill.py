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

    def test_solve_small_array_max_moves(self):
        arr_len = 10
        move_count = pow(10, 5)
        self._assert_solve_array_with_single_significant_move(arr_len, move_count)

    def test_solve_max_array_small_moves(self):
        arr_len = pow(10, 9)
        move_count = 5
        self._assert_solve_array_with_single_significant_move(arr_len, move_count)

    def test_solve_max_array_max_moves(self):
        arr_len = pow(10, 9)
        move_count = pow(10, 5)
        self._assert_solve_array_with_single_significant_move(arr_len, move_count)

    def test_lcm(self):
        self.assertEqual(6, Case._lcm(2, 3))
        self.assertEqual(4, Case._lcm(2, 4))
        self.assertEqual(1, Case._lcm(1, 1))
        self.assertEqual(pow(10, 9), Case._lcm(2, pow(10, 9)))

    def _assert_solve_array_with_single_significant_move(self, arr_len, move_count):
        low_value = 1
        high_value = 2
        moves = list[Move]()
        for i in range(move_count):
            moves.append(Move(low_value, 3))
        moves.append(Move(high_value, arr_len + 1))
        self.assert_solve(Case(arr_len, moves), high_value * arr_len)

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
