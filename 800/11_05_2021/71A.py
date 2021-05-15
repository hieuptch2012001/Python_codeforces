def inputs():
    a = int(input())
    return a

def bodys(a):
    for i in range(a):
        i = input()
        if len(i) > 10:
            print(i[0], len(i) - 2, i[-1], sep="")
        else:
            print(i)

def main():
    a = inputs()
    bodys(a)

if __name__ == "__main__":
    main()