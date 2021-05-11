def main():
    a = int(input())
    b = a / 5
    if (a % 5) > 0:
        b = b + 1

    print(int(b))

if __name__ == "__main__":
    main()
