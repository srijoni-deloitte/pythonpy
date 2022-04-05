class appendToList:
    def append1(self, dict1):
        ans = []
        ##iterating over the keys of dicti
        for j in range(len(list(dict1.keys()))):
            temp = []
            ##now for all the dicti.keys..lets append in temp
            temp.append(list(dict1.keys())[j])
            for k in range(len(list(dict1.values())[j])):
                temp.append(list(dict1.values())[j][k])
            ans.append(temp)
        return ans


mapi = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
send = appendToList()
print(send.append1(mapi))
