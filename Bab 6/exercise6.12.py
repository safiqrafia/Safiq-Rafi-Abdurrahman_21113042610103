
favorite_places = {
    "John": ["Paris", "Tokyo", "New York"],
    "Alice": ["London", "Sydney", "Rome"],
    "Bob": ["Barcelona", "Berlin", "Amsterdam"],
    "Charlie": ["Los Angeles", "Toronto", "Dubai", "Singapore"],
    "Jack": ["Moscow", "Beijing"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
    print(f"Total favorite places: {len(places)}")