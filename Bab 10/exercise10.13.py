
from pathlib import Path
import json

def ambil_info_pengguna_tersimpan(path):
    """Mengambil informasi pengguna yang sudah tersimpan jika tersedia."""
    if path.exists():
        isi = path.read_text()
        kamus_pengguna = json.loads(isi)
        return kamus_pengguna
    else:
        return None


def ambil_info_pengguna_baru(path):
    """Mengambil informasi dari pengguna baru."""
    nama_pengguna = input("Siapa namamu? ")
    permainan = input("Apa permainan favoritmu? ")
    hewan = input("Apa hewan favoritmu? ")

    kamus_pengguna = {
        'nama_pengguna': nama_pengguna,
        'permainan': permainan,
        'hewan': hewan,
    }

    isi = json.dumps(kamus_pengguna)
    path.write_text(isi)
    return kamus_pengguna


def sapa_pengguna():
    """Menyapa pengguna berdasarkan nama dan informasi yang diketahui."""
    path = Path('user_info.json')
    kamus_pengguna = ambil_info_pengguna_tersimpan(path)

    if kamus_pengguna:
        print(f"Selamat datang kembali, {kamus_pengguna['nama_pengguna']}!")
        print(f"Semoga kamu masih memainkan {kamus_pengguna['permainan']}.")
        print(f"Apakah kamu baru saja melihat {kamus_pengguna['hewan']}?")
    else:
        kamus_pengguna = ambil_info_pengguna_baru(path)
        pesan = (
            f"Kami akan mengingatmu ketika kamu kembali, "
            f"{kamus_pengguna['nama_pengguna']}!"
        )
        print(pesan)


sapa_pengguna()
