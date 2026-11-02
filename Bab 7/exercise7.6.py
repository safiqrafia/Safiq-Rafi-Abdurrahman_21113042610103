# 7-6 A. Conditional Test

print("\n--- 7-6 A. Conditional Test ---")

prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished: ) "

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")


# 7-6 B. Active Variable

print("\n--- 7-6 B. Active Variable ---")

prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' when you are finished: ) "

active = True

while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("You get in free!")
        elif age < 12:
            print("Your admission cost is $10.")
        else:
            print("Your admission cost is $15.")


# 7-6 C. Break Statement

print("\n--- 7-6 C. Break Statement ---")

prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished: ) "

while True:
    topping = input(prompt)

    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
    else:
        break