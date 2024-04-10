'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

'''
Created: 4/8/2024
Problem : dailycodingproblem.com

'''

inpArray = [1, 2, 3, 4, 5]

def findArray(inp):
    total = 1
    for i in inp:
        total = total * i
    for i in range(len(inp)):
        inp[i] = int(total/inp[i])
    return inp

print(findArray(inpArray))
