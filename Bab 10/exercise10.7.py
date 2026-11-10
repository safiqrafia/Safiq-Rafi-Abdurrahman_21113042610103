
print("Masukkan 'q' kapan saja untuk keluar.\n")

while True:
    try:
        angka_pertama = input("\nMasukkan sebuah angka: ")
        if angka_pertama == 'q':
            break

        angka_pertama = int(angka_pertama)

        angka_kedua = input("Masukkan angka lainnya: ")
        if angka_kedua == 'q':
            break

        angka_kedua = int(angka_kedua)

    except ValueError:
        print("Maaf, saya membutuhkan input berupa angka.")

    else:
        jumlah = angka_pertama + angka_kedua
        print(f"Jumlah dari {angka_pertama} dan {angka_kedua} adalah {jumlah}.")
