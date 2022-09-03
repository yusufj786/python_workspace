# Python program to extract digits from tuple list
from itertools import chain

myList = [(4, 62), (2, 65), (5, 9), (0,1)]
print("The list is : " + str(myList))

valMap = map(lambda ele: str(ele), chain.from_iterable(myList))
uniqueDigits = set()
for values in valMap:
	for digits in values:
		uniqueDigits.add(int(digits))

print("Unique digits of the set : " + str(uniqueDigits))