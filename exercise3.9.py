
# copied frrom exercise3.5.py
people = ["Robert", "John", "Alice"]

print(f"Hai {people[0]}, bisakah kamu datang untuk makan malam?")
print(f"Hai {people[1]}, bisakah kamu datang untuk makan malam?")
print(f"Hai {people[2]}, bisakah kamu datang untuk makan malam?")

print(f"{people[2]} tidak bisa datang untuk makan malam.")

people_length = len(people)

print(f"Saat ini ada {people_length} orang yang diundang untuk makan malam.")

people[2] = "David"

print(f"Hai {people[0]}, bisakah kamu datang untuk makan malam?")
print(f"Hai {people[1]}, bisakah kamu datang untuk makan malam?")
print(f"Hai {people[2]}, bisakah kamu datang untuk makan malam?")

people_length = len(people)

print(f"Saat ini ada {people_length} orang yang diundang untuk makan malam.")