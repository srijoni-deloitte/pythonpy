class Update:
    def Rename(self,dict1):
        dict1["city"] = "Location"
        print(dict1)

dict1 = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}
update=Update()
update.Rename(dict1)