def main():
    year = int(input())

    while True:
        year = year + 1
        if len(set(str(year))) == len(str(year)):
            break

    print(year)


if __name__ == "__main__":
    main()


# def func(n):
#     while True:
#         n = n + 1
#         if len(set(str(n))) == len(str(n)):
#             break

#     return n


# def test():
#     res = func(1987)
#     assert res == 2013


# def test2():
#     res = func(2013)
#     assert res == 2014
