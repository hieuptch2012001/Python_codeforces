def main():
    name = input()

    count = 0
    for i in name:
        if i.isupper():
            count = count + 1

    if count > (len(name) // 2):
        name = name.upper()
    else:
        name = name.lower()
    
    print(name)

if __name__ == "__main__":
    main()
