for _ in range(int(input())):
    n=int(input())
    s=input()
    firsta=s.find('A')
    lastb=s.rfind('B')
    if firsta < lastb and lastb != -1 and firsta != -1:
        ans= lastb - firsta
        print(ans)
    else:
        print(0)
