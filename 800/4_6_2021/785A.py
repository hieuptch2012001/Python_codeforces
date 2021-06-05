def main():
    n = int(input())
    count = 0
    for i in range(n):
        a = input()
        if a == 'Tetrahedron':
            count = count + 4
        elif a == 'Cube':
            count = count + 6
        elif a == 'Octahedron':
            count = count + 8
        elif a == 'Dodecahedron':
            count = count + 12
        elif a == 'Icosahedron':
            count = count + 20
        else:
            count = count + 0
    print(count)

if __name__ == '__main__':
    main()