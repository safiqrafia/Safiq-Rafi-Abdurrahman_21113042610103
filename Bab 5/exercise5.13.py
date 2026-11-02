# Student Grade Checker

name = input("Enter your name: ")
score = int(input("Enter your score: "))

print("Student Name:", name)
print("Student Score:", score)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

if score >= 75:
    print("Result: Passed!")
else:
    print("Result: Failed!")