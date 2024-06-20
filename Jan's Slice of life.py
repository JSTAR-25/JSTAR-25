# Jan's Slice of Life

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)



#print(num_two_dollar_slices)

#print(num_pizzas)

print("We sell", num_pizzas, "different kinds of pizza!")

# Pizzas & Prices

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.insert(1,[2.5, "peppers"])

pizza_and_prices.sort()

print(pizza_and_prices)

print("On a budget?, Find our cheapest pizza here...")
cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop()

three_cheapest = pizza_and_prices[0:3]
print(cheapest_pizza)

print("What's our 3 cheapest for you and your amigos you say??")
print(three_cheapest)












