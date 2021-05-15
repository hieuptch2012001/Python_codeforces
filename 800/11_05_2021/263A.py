def inputs():
    for i in range(5):
        a = [int(x) for x in input().split()]
        for j in range(5):
            if a[j] == 1:
                b = abs(2 - i) + abs(2 - j)
                print(b)
                break

def main():
    inputs()

if __name__ == "__main__":
    main()