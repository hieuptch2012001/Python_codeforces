def main():
    n, h = [int(x) for x in input().split()]

    b = [int(x) for x in input().split()]
    c = 0
    d = 0
    for i in b:
        if i <= h:
            c = c + 1
        else:
            c = c + 2

    print(c)


if __name__ == '__main__':
    main()
