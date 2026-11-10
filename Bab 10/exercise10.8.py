
from pathlib import Path

daftar_file = ['kucing.txt', 'anjing.txt']

for nama_file in daftar_file:
    print(f"\nMembaca file: {nama_file}")

    path = Path(nama_file)
    try:
        isi = path.read_text()
    except FileNotFoundError:
        print("  Maaf, saya tidak dapat menemukan file tersebut.")
    else:
        print(isi)
