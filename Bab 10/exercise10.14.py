
from pathlib import Path
import json


def ambil_nama_pengguna_tersimpan(path):
    """Mengambil nama pengguna yang sudah tersimpan jika tersedia."""
    if path.exists():
        isi = path.read_text()
        nama_pengguna = json.loads(isi)
        return nama_pengguna
    else:
        return None


def ambil_nama_pengguna_baru(path):
    """Meminta nama pengguna baru."""
    nama_pengguna = input("Siapa namamu? ")
    isi = json.dumps(nama_pengguna)
    path.write_text(isi)
    return nama_pengguna


def sapa_pengguna():
    """Menyapa pengguna berdasarkan namanya."""
    path = Path('username.json')
    nama_pengguna = ambil_nama_pengguna_tersimpan(path)

    if nama_pengguna:
        benar = input(f"Apakah kamu {nama_pengguna}? (y/n) ")

        if benar == 'y':
            print(f"Selamat datang kembali, {nama_pengguna}!")
            return

    # Meminta nama baru jika nama sebelumnya tidak sesuai.
    nama_pengguna = ambil_nama_pengguna_baru(path)
    print(
        f"Kami akan mengingatmu ketika kamu kembali, "
        f"{nama_pengguna}!"
    )


sapa_pengguna()
