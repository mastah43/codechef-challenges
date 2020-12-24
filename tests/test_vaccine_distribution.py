from unittest import TestCase
import subprocess
from typing import List
from vaccine_distribution.vaccine_distribution import Case


class Test(TestCase):
    def test_1(self):
        result = self.run_problem_solver(1, [1])
        self.assertEqual([1], result)

    def test_2(self):
        result = self.run_problem_solver(2, [6, 99, 25, 30])
        self.assertEqual([2], result)

    def test_example_1(self):
        result = self.run_problem_solver(1, [10, 20, 30, 40, 50, 60, 90, 80, 100, 1])
        self.assertEqual([10], result)

    def test_example_2(self):
        result = self.run_problem_solver(1, [9, 80, 27, 72, 79])
        self.assertEqual([3], result)

    def run_problem_solver(self, d: int, ages: List[int]) -> List[int]:
        return self.run_problem_solver_cases(cases=[Case(d=d, ages=ages)])

    def run_problem_solver_cases(self, cases: List[Case]) -> List[int]:
        proc = subprocess.Popen(
            ['python', 'vaccine_distribution.py'],
            cwd='../vaccine_distribution',
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)

        self.write_input(proc, cases)

        proc.stdin.close()
        proc.wait()
        output = list(self.read_output(proc))
        proc.stdout.close()
        return output

    def write_input(self, proc, cases: List[Case]):
        self.write_stdin_line(proc,  str(len(cases)) + '\n')
        for case in cases:
            self.write_input_case(proc, case)

    def write_input_case(self, proc, case: Case):
        self.write_stdin_line(proc, str(case.d) + ' ' + str(len(case.ages)) + '\n')
        self.write_stdin_line(proc, ' '.join([str(age) for age in case.ages]) + '\n')

    def write_stdin_line(self, proc, line: str):
        proc.stdin.write(bytes(line, 'utf-8'))

    def read_output(self, proc) -> List[int]:
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            yield int(line)
