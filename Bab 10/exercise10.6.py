
try:
    angka_pertama = input("Masukkan sebuah angka: ")
    angka_pertama = int(angka_pertama)

    angka_kedua = input("Masukkan angka lainnya: ")
    angka_kedua = int(angka_kedua)

except ValueError:
    print("Maaf, saya membutuhkan input berupa angka.")

else:
    jumlah = angka_pertama + angka_kedua
    print(f"Jumlah dari {angka_pertama} dan {angka_kedua} adalah {jumlah}.")
