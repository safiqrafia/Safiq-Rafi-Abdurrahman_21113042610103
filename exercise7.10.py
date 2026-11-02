
name_prompt = "\n What is your name? "
place_prompt = "\n If you could visit one place in the world, where would it be? "
continue_prompt = "\n Would you like to let someone else respond? (yes/no) "

responses = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat.lower() == 'yes':
        break

print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")