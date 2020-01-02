# Python soln for CodeSignal problem rotateImage. 
# Given an a two-dimensional list in python, the 
# function will output a rotated version of the
# array.
def rotateImage(a):
    output = []
    for row in a:
        for elem in row:
            print(elem, ' ')
        print(' ')
    return output

output = [[]]
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
output = rotateImage(a)
print(output)