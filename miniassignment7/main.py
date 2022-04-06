def operationcheck(res,secvalue):
    if secvalue=='+':
        return res[0]+res[1]
    elif secvalue=='-':
        return res[0]-res[1]
    elif secvalue=='*':
        return res[0]*res[1]
    else:
        try:
            ans=res[0]/res[1]
            return ans
        except ZeroDivisionError:
            print("division by zero is not possible")






def senditist(res):
    r=res.split('+')
    try:

        if len(r)!=3:
            raise Exception ("Formula exception")
    except Exception as e:
        print(e)
    try:
        r[0]=float(r[0])
        r[1]=float(r[1])
    except:
        print("something is wrong")


res=str(input())
secvalue=res[1]
senditist(res)
operationcheck(res,secvalue)