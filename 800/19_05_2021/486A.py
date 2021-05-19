# def main():
#     n = int(input())
#     a = 0
#     b = 0
#     for i in range(n+1):
#         if i % 2 == 0:
#             a = a + i
#         else:
#             b = b - i
#     print(a + b)

# if __name__ == "__main__":
#     main()

def main():
    n = int(input())
    if n % 2 == 0:
        a = n / 2
    if n % 2 == 1:
        a = (n-1)/2 - n
    print(int(a))

if __name__ == "__main__":
    main()