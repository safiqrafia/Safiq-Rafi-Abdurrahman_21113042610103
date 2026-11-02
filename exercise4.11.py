
pizzas = ["pepperoni", "cheese", "mushroom",]

friends_pizzas = pizzas[:]

# add new pizza to the original list
pizzas.append("hawaiian")

# add different pizza to the friend pizzas
friends_pizzas.append("veggie")

# prove the lists are separate

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)    