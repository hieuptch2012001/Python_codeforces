def main():
    n = int(input())
    a = 'I hate it'
    b = 'I hate that'
    c = 'I love it'
    d = 'I love that'
    for i in range(1,n):
        if i % 2 == 1:
            print(b,end=" ")
        else:
            print(d,end=" ")
    if n % 2 == 1:
        print(a,end=" ")
    if n % 2 == 0:
        print(c,end=" ")

if __name__ == "__main__":
    main()