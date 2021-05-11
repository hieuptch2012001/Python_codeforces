def main():
    a, b = [int(x) for x in input().split()]
    count = 1
    while True:
        a = a * 3
        b = b * 2
        if a > b:
            break
        else:
            count = count + 1
        
    print(count)

if __name__ == "__main__":
    main()  
