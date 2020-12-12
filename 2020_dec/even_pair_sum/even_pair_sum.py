import sys


def even_pair_count(a, b):
    assert 1 <= a <= 10**9
    assert 1 <= b <= 10**9
    count = 0
    for ai in range(1, a + 1):
        for bi in range(1, b + 1):
            if (ai + bi) % 2 == 0:
                print(str(ai) + '+' + str(bi))
                count = count + 1
    return count


def read_input():
    input_len = int(sys.stdin.readline())
    for i in range(1, input_len):
        line = sys.stdin.readline()
        if not line:
            break
        yield [int(x) for x in line.split()]

        yield int(line)


def main():
    pairs = read_input()
    for pair in pairs:
        count = even_pair_count(pair[0], pair[1])
        print(count)


if __name__ == "__main__":
    main()
