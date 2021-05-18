def main():
    n = int(input())
    count = 0
    for i in range(n):
        p, q = [int(x) for x in input().split()]
        if (q - p) >= 2:
            count = count + 1

    print(count)


if __name__ == '__main__':
    main()
