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
stairs = 5
#stairs = getStairCount()
largestCount = math.ceil(stairs/min(stepOptions))

def loops():
    pass