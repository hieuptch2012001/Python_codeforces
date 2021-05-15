def inputs():
    n = input()
    return n

def bodys(n):
    a = b = c = 0
    for i in range(0, len(n), 2):
        if n[i] == '1':
            a = a + 1
        elif n[i] == '2':
            b = b + 1
        else:   
            c = c + 1

    sum = '1+' * a + '2+' * b + '3+' * c
    print(sum[:-1])

def main():
    n = inputs()
    bodys(n)

if __name__ == "__main__":
    main()