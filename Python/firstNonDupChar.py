"""
This is a soln to the CodeSignal problem firstNotRepeatingCharacter. It takes in a String and returns the first non-duplicated character.
If there is no repeated character, it should return '_'. It should also utilize O(1) memory and only read the String once.  

Ex: s = "abacabad" -> firstNotRepeatingCharacter(s) = 'c'.
"""

def firstNotRepeatingCharacter(s):
    output = '_'

    # dict mapping the character to the amount of times it appears
    seenMap = {s[0]: 0}

    # index
    i = -1

    # update seenMap with correct amount of times read
    for x in s:
        i += 1
        if x in seenMap:
            seenMap[x] = seenMap.get(x) + 1
        else:
            tempMap = {s[i]: 1}
            seenMap.update(tempMap)

    # non-duplicated character has only been read once
    for y in seenMap:
        if seenMap.get(y) == 1:
            output = y
            return output

    return output

# default set to 0 for testing purposes (must be careful when choosing strings)
output = 0

output = firstNotRepeatingCharacter("abacabad")
print(output)