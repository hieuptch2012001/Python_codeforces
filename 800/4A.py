def inputs():
    a = int(input())
    return a

def body(a):
    if a <= 2:
        print("NO")
    elif a % 2 == 0:
        print("YES")
    else:
        print("NO")

def main():
    a = inputs()
    body(a)

if __name__ == "__main__":
    main()