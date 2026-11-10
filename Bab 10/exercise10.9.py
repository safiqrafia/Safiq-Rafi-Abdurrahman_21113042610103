
from pathlib import Path

daftar_file = ['kucing.txt', 'anjing.txt']

for nama_file in daftar_file:
    path = Path(nama_file)
    try:
        isi = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"\nMembaca file: {nama_file}")
        print(isi)
