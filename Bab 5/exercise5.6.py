

age = 4

if age < 2:
    print("Bayi")
elif age in range(2, 4):
    print("Balita")
elif age in range(4, 13):
    print("Anak-anak")
elif age >= 13 and age < 20:
    print("Remaja")
elif age >= 20 and age < 65:
    print("Dewasa")
else:
    print("Lansia")