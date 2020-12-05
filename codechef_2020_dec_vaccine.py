import argparse


def days_to_vaccine_number(d1, v1, d2, v2, p):
    assert 1 <= d1 <= 100
    assert 1 <= d2 <= 100
    assert 1 <= v1 <= 100
    assert 1 <= v2 <= 100
    assert 1 <= p <= 1000

    p_cur = 0
    day = 0
    while p_cur < p:
        day = day + 1
        if d1 <= day:
            p_cur += v1
        if d2 <= day:
            p_cur += v2

    return day


def parse_args():
    parser = argparse.ArgumentParser(description='Calculate days to vaccine production ammount.')
    parser.add_argument('d1', type=int)
    parser.add_argument('v1', type=int)
    parser.add_argument('d2', type=int)
    parser.add_argument('v2', type=int)
    parser.add_argument('p', type=int)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print(days_to_vaccine_number(args.d1, args.v1, args.d2, args.v2, args.p))


if __name__ == "__main__":
    main()
