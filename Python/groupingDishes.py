# Python solution for groupingDishes (codeSignal problem)


def groupingDishes(dishes):
    output = []
    dishDict = {"": []}
    
    # add each dish to the dictionary under ingredient
    for dish in dishes:
        i = -1

        for ingredient in dish:
            i += 1

            if i is not 0:
                if ingredient not in dishDict:
                    tempMap = {ingredient: [dish[0]]}
                    dishDict.update(tempMap)
                else:
                    dishDict[ingredient] = sorted(dishDict.get(ingredient) + [dish[0]])

    # add each qualifying entry (more than one dish uses the ingredient) to the output
    for entry in dishDict:
        if len(dishDict.get(entry)) > 1:
            tempList = [entry]

            for ingredient in dishDict.get(entry):
                tempList.append(ingredient)

            output.append(tempList)
    
    return sorted(output)

# initialize output as empty string
output = []

# call groupingDishes with testing string (from one of the failed test cases on CodeSignal)
dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]
output = groupingDishes(dishes) 

print(output)