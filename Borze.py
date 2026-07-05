s=input()
num=[]
l=0
r=len(s)-1
while l<=r:
    if s[l]=='-'  and s[l+1]=="-":
        num.append("2")
        l+=2
    elif s[l]=="-" and s[l+1]==".":
        num.append("1")
        l+=2
    elif s[l]==".":
        num.append("0")
        l+=1
print("".join(num))
