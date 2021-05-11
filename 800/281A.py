def inputs():
    n = input()
    return n

def bodys(n):
    print('' + n[0].upper() + n[1:])

def main():
    n = inputs()
    bodys(n)

if __name__ == "__main__":
    main()