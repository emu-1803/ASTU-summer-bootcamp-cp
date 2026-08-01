for _ in range(int(input())):
    n=int(input())
    if n<=3:
        print(n)
    elif n%2!=0:
        print(n%2)
    elif n%2==0 and n//3:
        print(0)
    else:
        print(n%3)
