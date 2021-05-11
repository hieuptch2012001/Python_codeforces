def inputs():
    m = input().lower()
    n = input().lower()
    return m, n


def bodys(m, n):
    if m == n:
        print('0')
    elif m > n:
        print('1')
    else:
        print('-1')


def main():
    m, n = inputs()
    bodys(m, n)


if __name__ == "__main__":
    main()
