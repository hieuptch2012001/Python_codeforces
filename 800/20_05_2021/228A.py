def main():
    a = [int(x) for x in input().split()]
    set_lst = set(a)
    print(4 - len(set_lst))


if __name__ == '__main__':
    main()
