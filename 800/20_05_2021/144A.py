def main():
    n = int(input())
    lst = [int(x) for x in input().split()]

    max_lst = max(lst)
    min_lst = min(lst)

    count = lst.index(max_lst)
    lst.pop(count)
    lst.insert(0, count)
    lst.reverse()

    count = count + lst.index(min_lst)
    print(count)


if __name__ == '__main__':
    main()
