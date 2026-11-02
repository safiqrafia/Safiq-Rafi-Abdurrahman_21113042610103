
def city_country(city, country):
    """Return a string like 'Magelang, Indonesia'."""
    return f"{city.title()}, {country.title()}"

city = city_country('magelang', 'indonesia')
print(city)

city = city_country('tokyo', 'japan')
print(city)

city = city_country('sydney', 'australia')
print(city)