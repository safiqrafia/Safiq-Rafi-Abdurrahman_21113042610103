
person_0 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York" 
}

person_1 = {
    "first_name": "James",
    "last_name": "Smith",
    "age": 25,
    "city": "London" 
}

person_2 = {
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 19,
    "city": "Sydney" 
}

people = [
    person_0,
    person_1,   
    person_2
]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()      