def main():
    n = int(input())
    a = []
    b = [int(x) for x in input().split()]
    for i in range(1, n+1):
        for j in range(n):
            if b[j] == i:
                print(j+1, end=" ")


if __name__ == '__main__':
    main()
