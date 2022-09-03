#Sort Dictionary key and values List
dict = {'gfg': [7, 6, 3], 
            'is': [2, 10, 3], 
            'best': [19, 4]}

print("The original dictionary is : " + str(dict))

res = {key : sorted(dict[key]) for key in sorted(dict)}
print("The sorted dictionary : " + str(res)) 