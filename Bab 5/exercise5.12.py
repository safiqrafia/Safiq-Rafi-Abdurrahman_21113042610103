# Conditional tests
number = 10

print("Is number == 10? I predict True.")
print(number == 10)

print("Is number == 'car'? I predict False.")
print(number == "car")

print("Is number > 5? I predict True.")
print(number > 5)

print("Is number <= 10? I predict True.")
print(number <= 10)

list_1 = ["apple", "orange"]
list_2 = ["apple", "orange"]

print("Is list_1 == list_2? I predict True.")
print(list_1 == list_2)

print("Is list_1 != list_2? I predict False.")
print(list_1 != list_2)


# Test equality and inequality with strings
string_1 = "Rakha"
string_2 = "Abi"

print("Is string_1 == string_2? I predict False.")
print(string_1 == string_2)

print("Is string_1 != string_2? I predict True.")
print(string_1 != string_2)


# Test using lower()
print("Is string_1 == string_1.lower()? I predict False.")
print(string_1 == string_1.lower())


# Numerical tests
number = 10

print("Is number == 10? I predict True.")
print(number == 10)

print("Is number != 10? I predict False.")
print(number != 10)

print("Is number > 10? I predict False.")
print(number > 10)

print("Is number < 10? I predict False.")
print(number < 10)

print("Is number >= 10? I predict True.")
print(number >= 10)

print("Is number <= 10? I predict True.")
print(number <= 10)


# Tests using and/or
print("Is number >= 10 AND even? I predict True.")
print(number >= 10 and number % 2 == 0)

print("Is number >= 10 AND odd? I predict False.")
print(number >= 10 and number % 2 != 0)

print("Is number >= 10 OR odd? I predict True.")
print(number >= 10 or number % 2 != 0)


# Tests using in/not in
list_1 = ["Michael", "David"]

print("Is 'Paul' in list_1? I predict False.")
print("Paul" in list_1)

print("Is 'Michael' in list_1? I predict True.")
print("Michael" in list_1)

print("Is 'Michael' not in list_1? I predict False.")
print("Michael" not in list_1)


# Alien Colors
alien_color = "green"

if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 1 point!")