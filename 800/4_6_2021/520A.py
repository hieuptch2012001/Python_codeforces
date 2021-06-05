def main():
    n = int(input())
    lst = input()

    set_lst = set(lst.lower())

    if len(set_lst) == 26:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()