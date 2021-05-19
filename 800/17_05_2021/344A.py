def main():
    n = int(input())
    a = "00"
    b = 0

    for i in range(n):
        c = input()
        if a != c:
            b = b + 1
        
        a = c
    
    print(b)

if __name__ == '__main__':
    main()