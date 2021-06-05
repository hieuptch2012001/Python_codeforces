def main():
    a = input()
    b = input()
    c = input()
    lst = a + b

    if len(lst) != len(c): 
        print("NO")
        exit()
    else:
        for i in lst:
            if lst.count(i) != c.count(i):
                print("NO")
                exit()
    
    print("YES")
    
if __name__ == '__main__':
    main()