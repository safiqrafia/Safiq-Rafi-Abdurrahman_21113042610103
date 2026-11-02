
places = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Bali"]

print(places)

new_list = sorted(places) #mengurutkan list secara ascending

print(new_list)

new_list_reversed = sorted(places, reverse=True) #mengurutkan list secara descending

print(new_list_reversed)

places.reverse() #membalik urutan list

print(places)

places.reverse() #membalik urutan list kembali ke semula

print(places)

places.sort() #mengurutkan list secara ascending

print(places)

places.sort(reverse=True) #mengurutkan list secara descending

print(places)