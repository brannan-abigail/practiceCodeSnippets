# Python soln to CodeSignal problem containsDuplicates 
# based upon soln given by other member using sets
def containsDuplicates(a):
    return len(set(a)) != len(a)
    
output = False
a = [1, 2, 3, 1]
output = containsDuplicates(a)
print(output)