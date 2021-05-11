def main():
    a,b,c = [int(x) for x in input().split()]
    
    count = 0
    for i in range(c):
        count = count + (i + 1) * a

    if (count - b) > 0:
        print(count - b)
    else:
        print("0")

if __name__ == "__main__":
    main()