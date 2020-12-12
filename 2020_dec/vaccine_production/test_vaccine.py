from unittest import TestCase
import subprocess
import os


class Test(TestCase):
    def test_1(self):
        result = self.run_problem_solver(1, 2, 1, 3, 14)
        self.assertEqual(result, b'3\n')

    def test_2(self):
        result = self.run_problem_solver(5, 4, 2, 10, 100)
        self.assertEqual(result, b'9\n')

    def run_problem_solver(self, d1, v1, d2, v2, p):
        proc = subprocess.Popen(
            ['python', 'vaccine.py'],
            cwd=os.path.dirname(os.path.realpath(__file__)),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)
        input_line = str(d1) + ' ' + str(v1) + ' ' + str(d2) + ' ' + str(v2) + ' ' + str(p) + '\n'
        proc.stdin.write(bytes(input_line, 'utf-8'))
        proc.stdin.close()
        proc.wait()
        output = proc.stdout.readline()
        proc.stdout.close()
        return output
