def findSums(k, values):
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i] + values[j] == k: print(f'{values[i]} + {values[j]} == {k}')

findSums(10, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))