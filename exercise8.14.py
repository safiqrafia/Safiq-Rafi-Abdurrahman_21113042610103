
def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


my_pajero = make_car(
    'mitsubishi', 'pajero sport',
    color='black', year=2023, transmission='automatic'
)
print(my_pajero)

my_civic = make_car(
    'honda', 'civic turbo',
    color='white', year=2020, transmission='automatic'
)
print(my_civic)