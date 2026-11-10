
from pathlib import Path

# 1. Membaca dan menampilkan isi pi_digits.txt
print("=== MEMBACA FILE DIGIT PI ===")

path = Path('pi_digits.txt')
isi = path.read_text()

for baris in isi.splitlines():
    print(baris)


# 2. Membaca satu juta digit pi
print("\n=== SATU JUTA DIGIT PERTAMA PI ===")

path = Path('pi_million_digits.txt')
isi = path.read_text()

string_pi = ''
for baris in isi.splitlines():
    string_pi += baris.lstrip()

print(f"{string_pi[:52]}...")
print(f"Jumlah karakter: {len(string_pi)}")


# 3. Memeriksa apakah tanggal lahir terdapat dalam digit pi
print("\n=== PEMERIKSAAN TANGGAL LAHIR ===")

tanggal_lahir = input(
    "Masukkan tanggal lahir dengan format bulan tanggal tahun (contoh: 040122): "
)

if tanggal_lahir in string_pi:
    print("Tanggal lahir Anda ditemukan dalam satu juta digit pertama pi!")
else:
    print("Tanggal lahir Anda tidak ditemukan dalam satu juta digit pertama pi.")
