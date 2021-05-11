def inputs():
    a = int(input())
    b = input()
    return a, b

def bodys(a,b):
    count = 0
    for i in range(1,a):
        if b[i-1] == b[i]:
            count = count + 1
    print(count)

def main():
    a,b = inputs()
    bodys(a,b)

if __name__ == "__main__":
    main()