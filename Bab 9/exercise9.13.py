from random import randint


class Dadu:
    """Merepresentasikan sebuah dadu yang dapat dilempar."""

    def __init__(self, sisi=6):
        """Menginisialisasi dadu."""
        self.sisi = sisi

    def lempar_dadu(self):
        """Mengembalikan angka antara 1 dan jumlah sisi dadu."""
        return randint(1, self.sisi)


# Membuat dadu bersisi 6 dan menampilkan hasil dari 10 kali lemparan.
dadu_6 = Dadu()

hasil = []
for nomor_lemparan in range(10):
    hasil_lemparan = dadu_6.lempar_dadu()
    hasil.append(hasil_lemparan)

print("10 kali lemparan dadu bersisi 6:")
print(hasil)


# Membuat dadu bersisi 10 dan menampilkan hasil dari 10 kali lemparan.
dadu_10 = Dadu(sisi=10)

hasil = []
for nomor_lemparan in range(10):
    hasil_lemparan = dadu_10.lempar_dadu()
    hasil.append(hasil_lemparan)

print("\n10 kali lemparan dadu bersisi 10:")
print(hasil)


# Membuat dadu bersisi 20 dan menampilkan hasil dari 10 kali lemparan.
dadu_20 = Dadu(sisi=20)

hasil = []
for nomor_lemparan in range(10):
    hasil_lemparan = dadu_20.lempar_dadu()
    hasil.append(hasil_lemparan)

print("\n10 kali lemparan dadu bersisi 20:")
print(hasil)