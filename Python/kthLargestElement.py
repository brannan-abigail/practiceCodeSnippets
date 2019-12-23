# Python solution for kthLargestElement (codeSignal problem).
# It was included in the heaps, stacks and queues section, 
# though one wasn't needed.

def kthLargestElement(nums, k):
    nums.sort(reverse = True)
    return nums[k-1]

output = []

nums = [7, 6, 5, 4, 3, 2, 1]
k = 2
output = kthLargestElement(nums, k)
print(output)