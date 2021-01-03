from unittest import TestCase
import subprocess
from typing import List
from lead_game.lead_game import Game, lead_game


class Test(TestCase):

    def test_1(self):
        result = lead_game([
            Game(1, 2)
        ])
        self.assertEqual([2, 1], result)

    def test_2(self):
        result = lead_game([
            Game(2, 1)
        ])
        self.assertEqual([1, 1], result)

    def test_3(self):
        result = lead_game([
            Game(1, 4),
            Game(4, 0),
            Game(3, 0)
        ])
        self.assertEqual([1, 4], result)

    def test_main_example_1(self):
        result = self.run_problem_solver([
            Game(140, 82),
            Game(89, 134),
            Game(90, 110),
            Game(112, 106),
            Game(88, 90)
        ])
        self.assertEqual([1, 58], result)

    def run_problem_solver(self, games: List[Game]) -> (int, int):
        proc = subprocess.Popen(
            ['python', 'lead_game.py'],
            cwd='../lead_game',
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE)

        self.write_input(proc, games)

        proc.wait()
        output = self.read_output(proc)
        proc.stdout.close()
        return output

    def write_input(self, proc, games: List[Game]):
        self.write_stdin_line(proc, str(len(games)) + '\n')
        for game in games:
            self.write_input_game(proc, game)
        proc.stdin.close()

    def write_input_game(self, proc, game: Game):
        self.write_stdin_line(proc, str(game.p1_score) + ' ' + str(game.p2_score) + '\n')

    def write_stdin_line(self, proc, line: str):
        proc.stdin.write(bytes(line, 'utf-8'))

    def read_output(self, proc) -> (int, int):
        return [int(x) for x in proc.stdout.readline().split()]
