from unittest import TestCase
import subprocess
from typing import List
from olympics_ranking.olyrank import Case
from olympics_ranking.olyrank import olyrank


class Test(TestCase):
    def test_main_example_1(self):
        result = self.run_problem_solver([
            "3",
            "10 20 30 0 29 30",
            "0 0 0 0 0 1",
            "1 1 1 0 0 0"])
        self.assertEqual([1, 2, 1], result)

    def run_problem_solver(self, lines: List[str]) -> List[int]:
        proc = subprocess.Popen(
            ['python', 'olyrank.py'],
            cwd='../olympics_ranking',
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
