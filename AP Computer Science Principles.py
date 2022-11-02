print("*** Welcome to Ramen Restaurant ***")
print(" ")
print("                ---MENU---")
print("| Tonkotsu Ramen 15$ | Shoyu Ramen 15$ |")
print("| Miso Ramen 10$     | Drinks 3$       | ")
print("                   * * *")

food_selection = ["Tonkotsu ramen", "Shoyu ramen", "Shio ramen","Miso ramen", "Drinks"]
costs = [20, 15, 10, 3]

your_price = []
your_order = []
count = 0
total = 0

order = input("Can I take your order ? ")
if order =="no":
    exit()
else:
    print("Thanks you")
continue_order = True


while(continue_order == True):
    food_order = input("Please enter your order: ")

    if food_order == "tonkotsu ramen":
            your_order.append(food_selection[0])
            your_price.append(costs[0])
            count = count + 1
            total = total + (costs[0])

    elif food_order == "shoyu ramen":
            your_order.append(food_selection[1])
            your_price.append(costs[1])
            count = count + 1
            total = total + costs[1]

    elif food_order == "shio ramen":
            your_order.append(food_selection[2])
            your_price.append(costs[1])
            count = count + 1
            total = total + costs[1]

    elif food_order == "miso ramen":
            your_order.append(food_selection[3])
            your_price.append(costs[2])
            count = count + 1
            total = total + costs[2]

    elif food_order == "drinks":
            your_order.append(food_selection[4])
            your_price.append(costs[3])
            count += 1
            total = total + costs[3]
    else:
        print("The item you ordered is not ont the menu")

    end = input("Have you finished your orders ? ")
    if(end == "yes"):
        continue_order = False
    else:
        continue_order = True

def information(receipt):
    print("-----------")
    n = 0
    while (n<count):
        if receipt == your_order:
            print("Item: " + str(receipt[n]))
            n = n+1
        else :
            print("Cost: " + str(receipt[n]) + "$")
            n = n + 1

print(" ")
print("Here is your order")
information(your_order)
information(your_price)

print("-----------")
print("The final cost is " + str(total) + "$")