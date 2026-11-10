
from pathlib import Path

path = Path('guest_book.txt')

perintah = "\nHalo, siapa namamu? "
perintah += "\nMasukkan 'quit' jika kamu adalah tamu terakhir. "

daftar_nama_tamu = []

while True:
    nama = input(perintah)

    if nama == 'quit':
        break

    print(f"Terima kasih {nama}, namamu akan kami tambahkan ke buku tamu.")
    daftar_nama_tamu.append(nama)

# Membuat string dengan menambahkan "\n" setelah setiap nama.
string_file = ''

for nama in daftar_nama_tamu:
    string_file += f"{nama}\n"

path.write_text(string_file)
