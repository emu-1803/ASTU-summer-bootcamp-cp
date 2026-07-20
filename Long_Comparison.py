t = int(input())

for _ in range(t):

    x1, p1 = input().split()
    p1 = int(p1)

    x2, p2 = input().split()
    p2 = int(p2)

    l1 = len(x1) + p1
    l2 = len(x2) + p2

    if l1 > l2:
        print(">")
    elif l1 < l2:
        print("<")
    else:

        while len(x1) < len(x2):
            x1 += "0"

        while len(x2) < len(x1):
            x2 += "0"

        if x1 > x2:
            print(">")
        elif x1 < x2:
            print("<")
        else:
            print("=")
