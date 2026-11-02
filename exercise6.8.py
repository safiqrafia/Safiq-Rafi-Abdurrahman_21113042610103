
pet_0 = {
    "kind": "dog",
    "owner": "John",
    "weight": 20,
}

pet_1 = {
    "kind": "cat",
    "owner": "Alice",
    "weight": 5,
}

pet_2 = {
    "kind": "parrot",
    "owner": "Bob",
    "weight": 0.1,
}

pets = [
    pet_0,
    pet_1,
    pet_2
]

for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print()