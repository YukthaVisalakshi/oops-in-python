#math evaluation on get item setitem
'''code to add the sum of rows in a 2-d list'''
class RowSum:
    def __init__(self, matrix):
        self.matrix=matrix
    def __getitem__(self, row):
        return sum(self.matrix[row])
    def __setitem__(self, row, new_row):
        self.matrix[row]=new_row

m=RowSum([[1,2], [3,4], [5,6]])
#sum of 0 index row values=3
#sum of 2 index row values=11

print("Sum of row 0: ",m[0])
print("Sum of row 2: ",m[2])
m[1]=[10,20]

#sum of 1 index row values, which are new=30
print("New sum of row: ",m[1])