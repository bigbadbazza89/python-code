recipe = input("Name of Recipe> ")

portions = int(input("Number of Portions> "))

ingredient_cost_list = []

while True:
    ingredient_name = input("Ingredient> ")
    ingredient_weight = input("Total Weight(grams)> ")
    ingredient_cpk = (float(input("Ingredient Cost($)/kilo> ")) / 1000)
    reply = input("Keep going? (y/n)> ")
    total_cost = (float(ingredient_weight) * float(ingredient_cpk))
    ingredient_cost_list.append(float(total_cost))
    if reply == "n":
        break


print(("$" + str(round((sum(ingredient_cost_list) / portions) , 2)) + " per portion"))
