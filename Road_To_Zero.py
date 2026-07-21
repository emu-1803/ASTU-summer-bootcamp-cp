
for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    choice1= x *a + y*a
    choice2= min(x,y)*b + (max(x,y)- min(x,y))*a
    print min(choice1,choice2)
