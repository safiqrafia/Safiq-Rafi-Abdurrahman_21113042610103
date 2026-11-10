"""Kumpulan kelas untuk merepresentasikan akun administrator."""

from pengguna2 import Pengguna


class Administrator(Pengguna):
    """Pengguna yang memiliki hak akses administratif."""

    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        """Menginisialisasi administrator."""
        super().__init__(nama_depan, nama_belakang, nama_pengguna, email, lokasi)

        # Menginisialisasi daftar hak akses yang kosong.
        self.hak_akses = HakAkses()


class HakAkses:
    """Kelas untuk menyimpan hak akses administrator."""

    def __init__(self, hak_akses=None):
        """Menginisialisasi daftar hak akses."""
        if hak_akses is None:
            self.hak_akses = []
        else:
            self.hak_akses = hak_akses

    def tampilkan_hak_akses(self):
        """Menampilkan daftar hak akses administrator."""
        print("\nHak Akses:")
        if self.hak_akses:
            for hak in self.hak_akses:
                print(f"- {hak}")
        else:
            print("- Pengguna ini belum memiliki hak akses.")