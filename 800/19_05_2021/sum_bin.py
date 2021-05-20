def bin_decimal(a):
    decimal = 0
    for digit in a:
        decimal = decimal*2 + int(digit)

    return decimal


def main():
    a = input()
    b = input()
    a1 = bin_decimal(a)
    b1 = bin_decimal(b)
    c = a1 + b1
    print(bin(c)[2:])


if __name__ == "__main__":
    main()
