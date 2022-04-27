unsorted = [14, 6, 3, 2, 4, 15, 11, 8, 1, 7, 2, 1, 3, 4, 10, 22, 20]

for j in range(1, len(unsorted)):
    for i in range (1, len(unsorted)):
        if unsorted[i] < unsorted[i-1]:
            temp = unsorted[i-1]
            unsorted[i-1] = unsorted[i]
            unsorted[i] = temp
print(unsorted)