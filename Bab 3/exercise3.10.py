cities = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Medan"]

# len()

print(f"Jumlah kota dalam list adalah {len(cities)}")

# sort

cities.sort()

print(f"Daftar kota yang telah diurutkan adalah: {cities}")

reversed_cities = sorted(cities, reverse=True)

print(f"Daftar kota yang telah diurutkan terbalik adalah: {reversed_cities}")

cities.reverse()

print(f"Daftar kota yang telah diurutkan terbalik adalah: {cities}")

removed_element = cities.pop()

print(f"Kota yang dihilangkan adalah {removed_element}.")