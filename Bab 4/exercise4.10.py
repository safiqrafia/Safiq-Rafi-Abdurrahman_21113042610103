
cubes = [val**3 for val in range(1, 11)]
print(cubes)
# slice[start:stop(exclusive):step(negative=reverse)]

# first three
print("The first three items in the list are:")
fisrt_three = cubes[:3]
print(fisrt_three)

# middle three
print("The middle three items in the list are:")
middle_three = cubes[3:6]
print(middle_three)

# last three
print("The last three items in the list are:")
last_three = cubes[-3:]
print(last_three)
