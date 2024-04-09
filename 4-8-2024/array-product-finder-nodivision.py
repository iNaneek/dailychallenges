import copy

inpArray = [3, 2, 1]

def findArray(inpList):
    newList = [] #[0]*len(inpList)
    for i in range(len(inpList)):
        temp = copy.deepcopy(inpList)
        del temp[i]
        total = 1
        for i in temp:
            total = total * i
        newList.append(total)
    return newList


print(findArray(inpArray))