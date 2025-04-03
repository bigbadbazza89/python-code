####### DO NOT TOUCH ###########
content = """items,quantity,cost
banana,3,3.50
apple,2,1.50
rockmelon,1,4.50"""
with open("my_data.csv", "w") as f:
    f.write(content)
##### YOUR CODE STARTS BELOW ####
with open("my_data.csv", "r") as f:
    lines = f.readlines()

totals = []
for line in lines[1:]:

    items, quantity, cost = line.strip().split(",")
    quantity = int(quantity)
    cost = float(cost)
    total_cost = quantity * cost
    totals.append(f"{items.capitalize()}= {total_cost: .2f}")



    # banana_split = file[0]
    # banana_list = banana_split.split(",")
    # apple_split = file[1]
    # apple_list = apple_split.split(",")
    # rockmelon_split = file[2]
    # rockmelon_list = rockmelon_split.split(",")
    # banana_quant = int(banana_list[1])
    # apple_quant = int(apple_list[1])
    # rockmelon_quant = int(rockmelon_list[1])
    # banana_cost = float(banana_list[2])
    # apple_cost = float(apple_list[2])
    # rockmelon_cost = float(rockmelon_list[2])
    # banana_total = banana_cost * banana_quant
    # apple_total = apple_cost * apple_quant
    # rockmelon_total = rockmelon_cost * rockmelon_quant


with open("my_data.csv", "a") as ammended:
    ammended.write("\nTotal Cost: \n" + "\n".join(totals))
#     ammended.write("Total Cost: " + "\nBanana= " + str(banana_total) + "\nApple= " + str(apple_total) + "\nRockmelon= " + str(rockmelon_total))

# open the file my_data.csv  and calculate total cost and write the result to the file:

# (1) open the file in read mode
# (2) skip the first line
# (3) split each line into its elements
# (4) convert the numbers to floats/ints
# (5) multiply cost x quantity
# (6) sum total cost
# (7) open the file in append mode, and add the total cost

