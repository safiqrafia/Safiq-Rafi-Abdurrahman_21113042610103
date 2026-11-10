from random import choice

kemungkinan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

tiket_pemenang = []
print("Mari kita lihat seperti apa tiket yang menang...")


while len(tiket_pemenang) < 4:
    item_terpilih = choice(kemungkinan)


    if item_terpilih not in tiket_pemenang:
        print(f"  Kita mendapatkan {item_terpilih}!")
        tiket_pemenang.append(item_terpilih)

print(f"\nTiket pemenang akhirnya adalah: {tiket_pemenang}")