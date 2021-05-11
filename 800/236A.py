def main():
    a = input()
    set_a = set(a)

    if len(set_a) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')

if __name__ == "__main__":
    main()
    