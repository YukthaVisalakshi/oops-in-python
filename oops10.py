class Numbers:
    def __init__(self,mylist):
        self.myList=mylist
    def __getitem__(self, index):
        return self.myList[index]
    def __setitem__(self, index, val):
        self.myList[index]=val
NumList=Numbers([1,2,3,4,5,6,7,8,9,10])
print(NumList[5])
NumList[6]=100
print(NumList.myList)