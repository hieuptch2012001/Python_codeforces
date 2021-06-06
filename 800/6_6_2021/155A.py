def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    max = a[0]
    min = a[0]
    b = 0
    
    for i in range(n):
        if a[i] > max:
            max = a[i]
            b = b + 1
    
        if a[i] < min:    
            min = a[i]
            b = b + 1

    
    print(b)

if __name__ == '__main__':
    main()