# stringclass to take a string as input and then initialize it completely
class StringClass():
    def __init__(self):
        self.string = ""

    def get(self):
        stringini = self.string = "1234567"
        return stringini

    def getlen(self):
        return len(self.string)

    def converttochar(self):
        toarray = [i for i in self.string]
        return toarray


# find all the possible pairs in the string

class new():

    def findallpossiblepairs(self, n):
        array = []
        for i in range(len(n)):
            for j in range(len(n)):
                array.append((n[i], n[j]))
        print(array)
        return array

    # find the equal pairs in them whose sum is equal to something in mapi by mapi commands
    def findequal1(self, array):
        mapi = {}
        findequal = []
        for u, v in array:
            s = u + v
            if s not in mapi:
                mapi[s] = 1
            else:
                findequal.append((u, v))
        return findequal


obj = StringClass()
n = obj.get()
# get all the objects of string class ist
length = obj.getlen()
# get the length of the string
charactersplit = obj.converttochar()
# split the string into characters
m = new()
possiblecoordination = m.findallpossiblepairs(n)
# creating a newclass and find the possible pairs..and common elements whose sum by storing in dictionary
print(m.findequal1(possiblecoordination))
