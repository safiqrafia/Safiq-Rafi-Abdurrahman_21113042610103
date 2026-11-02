
def describe_city(city, country='Indonesia'):
    """Describe a city"""
    message =f"{city.title()} is in {country.title()}."
    print(message)

describe_city('Jakarta')
describe_city('Tokyo', 'Japan')
describe_city('Yogyakarta')