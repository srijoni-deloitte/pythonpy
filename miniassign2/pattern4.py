n=6
###let n be any no. from 1,n to be the rows
for r in range(0,n):
    for c in range(0,n):
        if r==0 or c==n-1 or r==c:
            print('*',end="")
        else:
            print(end=" ")
    print()