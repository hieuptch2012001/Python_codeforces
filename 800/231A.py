def inputs():
    n = int(input())
    return n

def bodys(n):
    count = 0
    for i in range(n):
        a = input()
        if a.count('1') >= 2:
            count = count + 1
    print(count)

def main():
    n = inputs()
    bodys(n)

if __name__ == "__main__":
    main()