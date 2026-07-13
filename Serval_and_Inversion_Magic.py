t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    dt = []

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            dt.append(i)

    if not dt:
        print("Yes")
    elif dt[-1] - dt[0] + 1 == len(dt):
        print("Yes")
    else:
        print("No")
