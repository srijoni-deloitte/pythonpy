def duplicate(NewValue):
    getone = {}
    ##here getone will take all the elements with their freq.
    for i in range(len(NewValue)):
        mapi = {}
        ##mapi would be updated at each point of time
        for j in NewValue[i]:
            if j not in mapi:
                mapi[j] = 1
            else:
                mapi[j] = mapi[j] + 1
        for j in mapi.keys():
            if mapi[j] > 1:
                getone[j] = mapi[j]
    return getone


value = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
findDuplicate = duplicate(value)
print(findDuplicate)
