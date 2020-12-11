from unittest import TestCase
import subprocess


class Test(TestCase):
    def test_main_1(self):
        result = self.run_main(1, 2, 1, 3, 14)
        self.assertEqual(result.stdout.readline(), b'3\n')

    def test_main_2(self):
        result = self.run_main(5, 4, 2, 10, 100)
        self.assertEqual(result.stdout.readline(), b'9\n')

    def run_main(self, d1, v1, d2, v2, p):
        proc = subprocess.Popen(['python', 'codechef_2020_dec_vaccine.py', str(d1), str(v1), str(d2), str(v2), str(p)],
                                stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        input_line = str(d1) + ' ' + str(v1) + ' ' + str(d2) + ' ' + str(v2) + ' ' + str(p) + '\n'
        proc.stdin.write(bytes(input_line, 'utf-8'))
        proc.stdin.close()
        #proc.communicate(input=bytes(input_line, 'utf-8'))
        return proc
