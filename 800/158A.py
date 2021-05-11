def inputs():
    n, k = [int(x) for x in input().split()]
    return n, k


def bodys(k):
    a = [int(x) for x in input().split()]
    tem = a[k - 1]
    count = 0
    for i in range(0, len(a)):
        if a[i] >= tem and a[i] > 0:
            count = count + 1
    print(count)


def main():
    n, k = inputs()
    bodys(k)


if __name__ == "__main__":
    main()
