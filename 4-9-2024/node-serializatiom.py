'''
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''

'''
Created: 4/9/2024
Problem : dailycodingproblem.com

'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(obj):
    tree = '[' + obj.val + ','

    if isinstance(obj.left, Node):
        tree += serialize(obj.left)
    elif obj.left:
        tree += obj.left
    else:
        tree += "%%%"

    tree += ','

    if isinstance(obj.right, Node):
        tree += serialize(obj.right)
    elif obj.right:
        tree += obj.right
    else:
        tree += "%%%"

    return tree + ']'

def deserialize(serial):
    node = Node(serial.split(',')[0][1:])

    bracketCounter = 0
    for indx, i in enumerate(serial[len(serial.split(',')[0]) + 1:-1]):
        if i == '[':
            bracketCounter += 1
        if i == ']':
            bracketCounter -= 1
        if i == ',' and bracketCounter == 0:
            if serial[len(serial.split(',')[0]) + 1:-1][:indx] != '%%%':
                node.left = deserialize(serial[len(serial.split(',')[0]) + 1:-1][:indx])
            if serial[len(serial.split(',')[0]) + 1:-1][indx+1:] != '%%%':
                node.right = deserialize(serial[len(serial.split(',')[0]) + 1:-1][indx+1:])

    return node

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val)
