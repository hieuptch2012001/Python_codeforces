def main():
    n = int(input())
    while n > 0:
        a,b = [int(x) for x in input().split()]
        c = (b - a%b) % b
        print(c)
        n = n - 1

if __name__ == '__main__':
    main()
    