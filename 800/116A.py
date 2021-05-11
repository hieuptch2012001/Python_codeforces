def main():
    n = int(input())
    x = 0
    y = 0
    for i in range(n):
        a, b = [int(x) for x in input().split()]

        y = y - a
        y = y + b
        
        x = max(x, y)

    print(x)

if __name__ == "__main__":
    main()
