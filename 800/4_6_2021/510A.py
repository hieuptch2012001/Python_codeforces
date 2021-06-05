def main():
    a,b = [int(x) for x in input().split()]
    for i in range(1,a+1):
        if i % 4 == 2:
            for j in range(1,b):
                print('.',end="")
            print("#")
        elif i % 4 == 0:
            print("#",end="")
            for j in range(1,b):
                print('.',end="")
            print("")
        else:
            for j in range(1, b+1):
                print("#",end="")
            print("")

if __name__ == '__main__':
    main()