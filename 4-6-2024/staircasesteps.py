'''
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
'''

'''
Created: 4/6/2024
Problem : dailycodingproblem.com example problem

'''

import math

stepOptions = (1, 2, 3)  # input for all stair options
stairs = 10  # input for total stairs

largestCount = math.ceil(stairs/min(stepOptions))  # largest set of additions is always the smallest step diveded by the stair count
solutionsCounter = 0  # counter of solutions

solutionCanadits = []
def findAllOptions(wantedLength, stepOptions, currentVal = 0):
    global solutionsCounter

    if wantedLength == 0:
        return None

    for i in stepOptions:
        solutionCanadits.append(currentVal + i)
        if currentVal + i == stairs:
            solutionsCounter += 1
        findAllOptions(wantedLength - 1, stepOptions, currentVal + i)

findAllOptions(largestCount, stepOptions)
print(solutionCanadits)
print(len(solutionCanadits))

print(solutionsCounter)


