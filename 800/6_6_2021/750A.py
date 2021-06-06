def main():
    n,k = [int(x) for x in input().split()]
    a = 0
    b = 0
    for i in range(1,n+1):
        a = a + (5*i)
        if k + a <= 240:
            b = b + 1
        else:
            continue
    print(b)

if __name__ == '__main__':
    main()