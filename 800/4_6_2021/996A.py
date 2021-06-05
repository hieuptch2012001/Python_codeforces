def main():
    n = int(input())
    a = [100,20,10,5,1]
    # print(n // 100 + n % 100 // 20 + n % 20 // 10 + n % 10 // 5 + n % 5)
    count = 0
    for i in a:
        count = count + (n//i)
        n = n % i
    print(count)
    
if __name__ == '__main__':
    main()
