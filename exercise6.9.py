
favorite_places = {
    "John": ["Paris", "Tokyo", "New York"],
    "Alice": ["London", "Sydney", "Rome"],
    "Bob": ["Barcelona", "Berlin", "Amsterdam"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")