mat=[]
for i in range(5):
    row=list(map(int,input().split()))
    mat.append(row)
flag=False
for i in range(5):
    for j in range(5):
        if mat[i][j]==1:
            movr=abs(2-i)
            movc=abs(2-j)
            res=movr+movc
            print(res)
            flag=True
    if flag == True:
        break
