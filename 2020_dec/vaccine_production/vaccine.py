import sys


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


def main():
    d1, v1, d2, v2, p = [int(x) for x in sys.stdin.readline().split()]
    print(days_to_vaccine_number(d1, v1, d2, v2, p))


if __name__ == "__main__":
    main()
