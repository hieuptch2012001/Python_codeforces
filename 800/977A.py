def main():
    a, b = [int(x) for x in input().split()]
    for i in range(1, b+1):
        if (a % 10 == 0):
            a = a / 10
        else:
            a = a - 1
    print(int(a))


if __name__ == "__main__":
    main()
