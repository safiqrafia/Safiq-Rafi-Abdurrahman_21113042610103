
from pathlib import Path

def hitung_kata_umum(nama_file, kata):
    """Menghitung berapa kali kata muncul dalam teks."""

    path = Path(nama_file)
    try:
        isi = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        jumlah_kata = isi.lower().count(kata)
        pesan = f"'{kata}' muncul dalam {nama_file} sekitar {jumlah_kata} kali."
        print(pesan)


nama_file = 'Morrisot.txt'
hitung_kata_umum(nama_file, 'the')
