# python Program to Remove Duplicate Element From a List
def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
    
duplicate = [2, 4, 5, 10, 20, 2, 20, 4]
print(Remove(duplicate))