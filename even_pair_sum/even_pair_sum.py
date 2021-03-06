import sys


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def even_pair_count(a, b):
    assert 1 <= a <= 10 ** 9
    assert 1 <= b <= 10 ** 9

    a_odds = a // 2 + a % 2
    a_evens = a // 2
    b_odds = b // 2 + b % 2
    b_evens = b // 2

    count = a_evens * b_evens + a_odds * b_odds
    return count


def read_input():
    input_len = int(sys.stdin.readline())
    pairs = []
    # print_err("input len " + str(input_len))
    for i in range(0, input_len):
        line = sys.stdin.readline()
        if not line:
            break
        pairs = pairs + [[int(x) for x in line.split()]]
    # print_err("pairs " + str(pairs))
    return pairs


def main():
    pairs = read_input()
    for pair in pairs:
        count = even_pair_count(pair[0], pair[1])
        print(count)


if __name__ == "__main__":
    main()
