n = int(input())
for i in range(int(n)):
    s = input().lower()
    if len(s) > 10:
        print(s[0] + str(len(s)-2) + s[-1])
    else:
        print(s)
