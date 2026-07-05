for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()

    s1=s1.replace('B','G')
    s2=s2.replace('B','G')
    
    if s1 == s2:
        print("YES")
    else:
        print("NO")
