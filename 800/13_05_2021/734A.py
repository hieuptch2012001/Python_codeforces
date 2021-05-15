def main():
    n = int(input())
    a = input()
    lst = list(a)
    b1 = 0
    b2 = 0
    for j in range(n):
        if lst[j] == 'A':
            b1 = b1 + 1
        if lst[j] == 'D':
            b2 = b2 + 1

    if b1 > b2:
        print('Anton')
    elif b1 < b2:
        print('Danik')
    else:
        print('Friendship')


if __name__ == '__main__':
    main()
