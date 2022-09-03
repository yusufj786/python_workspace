# python program to create pyramid patterns of numbers till 10
rows = 10

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")