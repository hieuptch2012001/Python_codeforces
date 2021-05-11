def inputs():
    m, n = [int(x) for x in input().split()]
    return m, n


def bodys(m, n):
    a = (m*n) / 2
    print(int(a))


def main():
    m, n = inputs()
    bodys(m, n)


if __name__ == "__main__":
    main()
