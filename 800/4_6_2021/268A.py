def main():
    n = int(input())
    c = []
    d = []
    for i in range(n):
        a, b = [int(x) for x in input().split()]
        c.append(a)
        d.append(b)

    count = 0
    for x in c:
        for y in d:
            if x == y:
                count = count + 1
    print(count)
if __name__ == '__main__':
    main()