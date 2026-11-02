
prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished: ) "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
    else:
        break