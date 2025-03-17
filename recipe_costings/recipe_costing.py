recipe = input("Name of Recipe> ")

portions = input("Number of Portions> ")

ingredient_cost_list = []

while True:
    ingredient_name = input("Ingredient> ")
    ingredient_weight = input("Total Weight(grams)> ")
    ingredient_cpg = (float(input("Ingredient Cost($)/kilo> ")) / 1000)
    reply = input("Keep going? (y/n)> ")
    total_cost = (int(ingredient_weight) * float(ingredient_cpg))
    ingredient_cost_list.append(int(total_cost))
    if reply == "n":
        break


print("$" + str(sum(ingredient_cost_list) / int(portions)) + " per portion")
