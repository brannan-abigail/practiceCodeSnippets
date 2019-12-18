# Python solution for amendTheSentence (codeSignal problem requiring the user to parse a given
# string with CapitalLettersForNewWords). The output for this example should be "capital letters for new words". 
# 
# Soln relies on basic Python String functions (.lower(), string indexing, .isupper())


def amendTheSentence(s):
    # first letter of phrase only needs to be turned lowercase
    output = s[0].lower()

    # slice first letter off of s for use in function
    s = s[1:len(s)]
    print(s)

    # for each letter if capital letter add " " and lowercase version
    for letter in s:
        if (letter.isupper()):
            letter = " " + letter.lower()
        
        output = output + letter
    
    return output

# initialize output as empty string
output = ""

# call amendTheSentence with testing string (from one of the failed test cases on CodeSignal)
output = amendTheSentence("VizQEogigkRZJacVELulHjG") # VizQEogig
print(output)