"""
This is a soln to the CodeSignal problem firstDuplicate. It takes in an array and returns the first duplicated value.
Following the approach that works in O(len(a)) time based on the advice in Hint 1, in which the "seen" list is the 
same size as the given array. 0 in seen[x-1] indicates not a duplicate, and a 1 means that it's seen. 

Ex: a = [2, 1, 3, 5, 3, 2] -> firstDuplicate(a) = 3.
"""

def firstDuplicate(a):
    output = -1

    # create list of 0's representing all values in the given list
    seen = [0] * len(a)

    # if an element is in the read list already, it's a duplicate
    for x in a:
        if seen[x-1] != 0:
            output = x
            return x
        else: 
            seen[x-1] = 1
        print(seen)

    return output

# default set to 0 (must be careful to choose testcases that work with this)
output = 0

output = firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])
print(output)