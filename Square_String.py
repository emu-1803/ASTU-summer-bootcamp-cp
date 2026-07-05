t=int(input())

for i in range(t):
    s = input()
    length = len(s)
    
    if length %2 == 0:
        half=length//2
        if s[:half]==s[half:]:
            print("YES")
        else:
            print("NO")
    else:print("NO")
