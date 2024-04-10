'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

'''
Created: 4/7/2024
Problem : dailycodingproblem.com

'''

def findSums(k, values):
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i] + values[j] == k: print(f'{values[i]} + {values[j]} == {k}')

findSums(10, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))