
favorite_numbers = {
    "Alice": [3, 7, 9],
    "Bob": [2, 4, 6],
    "Charlie": [1, 5],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} likes the following numbers:")
    for number in numbers:
        print(f" {number}")