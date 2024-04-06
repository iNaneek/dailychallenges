import math
def getStairCount():
    stairCount = None
    while stairCount == None:
        try:
            stairCount = int(input("How many stairs:"))
        except:
            print("Please give integer value")
    return stairCount


stepOptions = (1, 2)
stairs = 4
#stairs = getStairCount()
largestCount = math.ceil(stairs/min(stepOptions))
#largestCount -= 1
solutions = 0

options = []
def findAllOptions(wantedLength, stepOptions, currentVal = 0):

    if wantedLength == 0:
        return None

    for i in stepOptions:
        options.append(currentVal + i)
        findAllOptions(wantedLength - 1, stepOptions, currentVal + i)

findAllOptions(largestCount, stepOptions)
print(options)
print(len(options))


for i in options:
    if i == stairs:
        solutions += 1

print(solutions)


