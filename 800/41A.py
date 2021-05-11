def main():
    m = input()
    n = input()
    if m[::-1] == n:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()