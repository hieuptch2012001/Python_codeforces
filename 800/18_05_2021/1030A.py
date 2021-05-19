def main():
    n = int(input())

    a = [int(x) for x in input().split()]

    if sum(a) == 0:
        print('EASY')
    else:
        print('HARD')


if __name__ == '__main__':
    main()
