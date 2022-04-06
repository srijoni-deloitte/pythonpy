file = open("hello.txt", "r")

###here take the input of file
Read = file.read()
fileWords = Read.split(" ")
maxWord = (max(fileWords, key=len))
print(maxWord)