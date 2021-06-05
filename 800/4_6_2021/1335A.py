import math

def main():
    n = int(input())
    while n:
        a = 0
        b = int(input())

        # ceil : làm tròn số lên
        a = math.ceil((b/2) - 1)  
        
        print(a)
        n = n - 1


if __name__ == '__main__':
    main()