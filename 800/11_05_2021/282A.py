def inputs():
    n = int(input())
    return n


def bodys(n):
    a = 0
    for i in range(n):
        k = input()
        if k[0] == '+' or k[1] == '+':
            a = a + 1
        else:
            a = a - 1
    print(a)


def main():
    n = inputs()
    bodys(n)


if __name__ == "__main__":
    main()
