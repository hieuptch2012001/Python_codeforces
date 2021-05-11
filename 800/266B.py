def main():
    a,b = [int(x) for x in input().split()]
    n = input()
    while b: 
        n = n.replace('BG', 'GB')
        b = b - 1
    print(n)

if __name__ == "__main__":
    main()