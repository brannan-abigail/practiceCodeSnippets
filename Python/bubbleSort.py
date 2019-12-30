# Python solution for bubbleSort (codeSignal problem).
# Most of the soln was provided, I needed to simply fill
# in what length was.

def bubbleSort(items):
    def swap(firstIndex, secondIndex):
        temp = items[firstIndex]
        items[firstIndex] = items[secondIndex]
        items[secondIndex] = temp

    #  length added below (only addition to given code)
    length = len(items)

    for i in range(length):
        j = 0
        stop = length - i
        while j < stop - 1:
            if items[j] > items[j + 1]:
                swap(j, j + 1)
            j += 1
    return items


output = []

items = [2, 4, 1, 5]
output = bubbleSort(items)
print(output)