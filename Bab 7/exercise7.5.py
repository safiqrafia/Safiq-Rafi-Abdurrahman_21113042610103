
prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' when you are finished: ) "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("You get in free!")
    elif age < 12:
        print("Your admission cost is $10.")
    else:
        print("Your admission cost is $15.")