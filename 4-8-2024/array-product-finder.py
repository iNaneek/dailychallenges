inpArray = [1, 2, 3, 4, 5]

def findArray(inp):
    total = 1
    for i in inp:
        total = total * i
    for i in range(len(inp)):
        inp[i] = int(total/inp[i])
    return inp

print(findArray(inpArray))
