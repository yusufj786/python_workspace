#Create a list of tuples from given list having number and its cube in each tuple
List = [6, 2, 5 ,1, 4]

tupleList = [(val, (val*val*val)) for val in List]

print("The list of Tuples is : " , str(tupleList))