# 1. Fungsi make_shirt()

def make_shirt(size, message):
    """Summarize the shirt that is going to be made."""
    print(f"\nI'm going to make a {size} shirt.")
    print(f"It will say, '{message}'.")


make_shirt('Large', 'Cukup 2 Periode!')
make_shirt(message='Hidup Mahasiswa!', size='Medium')


# 2. Fungsi describe_city()

def describe_city(city, country='Indonesia'):
    """Describe a city."""
    message = f"{city.title()} is in {country.title()}."
    print(message)


describe_city('Jakarta')
describe_city('Tokyo', 'Japan')
describe_city('Yogyakarta')


# 3. Fungsi make_sandwich()

def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")

    for item in items:
        print(f"  ...adding {item} to your sandwich.")

    print("Your sandwich is ready!")


make_sandwich(
    'daging sapi',
    'keju slice',
    'selada',
    'sosis'
)

make_sandwich(
    'telur mata sapi',
    'tomat',
    'saus sambal'
)

make_sandwich(
    'susu kental manis',
    'meses'
)