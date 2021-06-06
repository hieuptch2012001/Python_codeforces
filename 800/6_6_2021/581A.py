import math

def main():
    a,b = [int(x) for x in input().split()]
    if a > b :
        max = a
        min = b
    elif a < b:
        max = b
        min = a
    else:
        print(a , '0')
        exit()

    sub = max - min

    day = math.floor(sub / 2)

    print(min,end=" ")
    print(day)
    
if __name__ == '__main__':
    main()