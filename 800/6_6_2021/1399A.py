def main():
    n = int(input())
    for i in range(n):
        a = int(input())
        b = [int(x) for x in input().split()]
        if (max(b) - min(b)) < len(b):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
