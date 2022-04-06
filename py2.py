
from functools import reduce
print("Enter the list")
##take the list in that matter
lst1=list(map(int,input("enter a list user input\n").split()))
##filter all elements whose value is negative
result=filter(lambda x:x<0,lst1)
##print the list
finalResult=list(result)
print(finalResult)
##multiply all two elements till it reduce to one
multiply=reduce(lambda x, y:x*y, finalResult)
print(multiply)
