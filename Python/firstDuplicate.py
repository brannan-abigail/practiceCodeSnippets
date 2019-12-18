"""
This is a soln to the CodeSignal problem firstDuplicate. It takes in an array and returns the first duplicated value.

Ex: a = [2, 1, 3, 5, 3, 2] -> firstDuplicate(a) = 3.
"""

def firstDuplicate(a):
    output = -1

    # record the elements that the program has read in order so that it knows when it's found a duplicate
    read = []

    # if an element is in the read list already, it's a duplicate
    for x in a:
        if x in read:
            output = x
            return output
        read.append(x)

    return output
    

# default set to 0 (must be careful to choose testcases that work with this)
output = 0

output = firstDuplicate([2, 1, 3, 5, 3, 2])
print(output)