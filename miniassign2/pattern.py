##ist part or upper part
for i in range(1,5):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n")

##lower part



for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n")
