
cities = {
    "Paris": {
        "country": "France",
        "population": 2_161_000,
        "fact": "Known for the Eiffel Tower."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 13_929_286,
        "fact": "The most populous city in the world."
    },
    "New York": {
        "country": "United States",
        "population": 8_336_817,
        "fact": "Home to the Statue of Liberty."
    }
}

for city, city_info in cities.items():
    country = city_info ["country"].title()
    population = city_info ["population"]
    fact = city_info ["fact"].title()

    print(f"\n{city.title()} is in {country}.")
    print(f" It has a population of about {population}.")
    print(f"This city is known for: {fact}")