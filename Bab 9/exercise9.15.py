from random import choice


def dapatkan_tiket_pemenang(kemungkinan):
    """Mengembalikan tiket pemenang dari sekumpulan kemungkinan."""
    tiket_pemenang = []


    while len(tiket_pemenang) < 4:
        item_terpilih = choice(kemungkinan)

        # Tambahkan item ke tiket pemenang hanya jika belum pernah terpilih.
        if item_terpilih not in tiket_pemenang:
            tiket_pemenang.append(item_terpilih)

    return tiket_pemenang


def periksa_tiket(tiket_yang_dimainkan, tiket_pemenang):
    """Memeriksa apakah tiket yang dimainkan merupakan tiket pemenang."""


    for elemen in tiket_yang_dimainkan:
        if elemen not in tiket_pemenang:
            return False


    return True


def buat_tiket_acak(kemungkinan):
    """Mengembalikan tiket acak dari sekumpulan kemungkinan."""
    tiket = []


    while len(tiket) < 4:
        item_terpilih = choice(kemungkinan)

    
        if item_terpilih not in tiket:
            tiket.append(item_terpilih)

    return tiket


kemungkinan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
tiket_pemenang = dapatkan_tiket_pemenang(kemungkinan)

jumlah_percobaan = 0
menang = False


maksimal_percobaan = 1_000_000

while not menang:
    tiket_baru = buat_tiket_acak(kemungkinan)
    menang = periksa_tiket(tiket_baru, tiket_pemenang)
    jumlah_percobaan += 1

    if jumlah_percobaan >= maksimal_percobaan:
        break


if menang:
    print("Kita mendapatkan tiket pemenang!")
    print(f"Tiket Anda: {tiket_baru}")
    print(f"Tiket pemenang: {tiket_pemenang}")
    print(f"Dibutuhkan {jumlah_percobaan} percobaan untuk menang!")
else:
    print(f"Sudah mencoba {jumlah_percobaan} kali, tetapi belum menang. :(")
    print(f"Tiket Anda: {tiket_baru}")
    print(f"Tiket pemenang: {tiket_pemenang}")