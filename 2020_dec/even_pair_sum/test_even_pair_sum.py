from unittest import TestCase
import subprocess
import os
import sys
from .even_pair_sum import even_pair_count


class Test(TestCase):
    def test_1_1(self):
        self.assertEqual(1, even_pair_count(1, 1))

    def test_1_2(self):
        self.assertEqual(1, even_pair_count(1, 2))
        self.assertEqual(1, even_pair_count(2, 1))

    def test_2_2(self):
        self.assertEqual(2, even_pair_count(2, 2))

    def test_2_3(self):
        self.assertEqual(3, even_pair_count(2, 3))
        self.assertEqual(3, even_pair_count(3, 2))

    def test_3_3(self):
        self.assertEqual(5, even_pair_count(3, 3))

    def test_4_6(self):
        self.assertEqual(12, even_pair_count(4, 6))

    def test_8_9(self):
        self.assertEqual(36, even_pair_count(8, 9))

    def test_main_simple(self):
        result = self.run_problem_solver([[8, 9]])
        self.assertEqual([36], result)

    def test_main_bound_max(self):
        result = self.run_problem_solver([[10**9, 10**9]])
        self.assertEqual([500000000000000000], result)

    def test_main_bound_min(self):
        result = self.run_problem_solver([[1, 1]])
        self.assertEqual([1], result)

    def test_main_official(self):
        result = self.run_problem_solver([
            [1, 1],
            [2, 3],
            [4, 6],
            [8, 9]
        ])
        self.assertEqual([1, 3, 12, 36], result)

    def run_problem_solver(self, pairs):
        proc = subprocess.Popen(
            ['python', 'even_pair_sum.py'],
            cwd=os.path.dirname(os.path.realpath(__file__)),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)

        self.write_input(pairs, proc)

        proc.stdin.close()
        proc.wait()
        output = list(self.read_output(proc))
        proc.stdout.close()
        return output

    def write_stdin_line(self, proc, line):
        proc.stdin.write(bytes(line, 'utf-8'))

    def write_input(self, pairs, proc):
        self.write_stdin_line(proc, str(len(pairs)) + '\n')
        for pair in pairs:
            assert len(pair) == 2
            self.write_stdin_line(proc, str(pair[0]) + ' ' + str(pair[1]) + '\n')

    def read_output(self, proc):
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            yield int(line)


