# Solution for singleNumber.py solution based on
# the CodeSignal singleNumber problem. Solution 
# taken from member's solution.

def singleNumber(nums):
    res = 0
    for num in nums:
        res ^= num
                
    return res

output = 0
nums = [2, 2, 1]
output = singleNumber(nums)
print(output)