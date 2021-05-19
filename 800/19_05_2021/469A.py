def main():
    lst1 = 'I become the guy.'
    lst2 = 'Oh, my keyboard!'
    
    n = int(input())
    p = input().split()[1:]
    q = input().split()[1:]

    set_pq = set(p+q)
    if len(set_pq) == n:
        print(lst1)
    else:
        print(lst2)

if __name__ == "__main__":
    main()


# n=int(input())
# x=input().split()[1:]
# y=input().split()[1:]
# print(['Oh, my keyboard!','I become the guy.'][len(set(x+y))==n])

#------------------------------------------------------------
# print('I become the guy.' if int(input()) <= len(set(input()[1:].split()) | set(input()[1:].split())) else 'Oh, my keyboard!')

#--------------------------------------------------------
#a=input;print("IO hb,e cmoym ek etyhbeo agrudy!."[int(a())>len(set(a().split()[1:]+a().split()[1:]))::2])