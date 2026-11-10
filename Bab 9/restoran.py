"""Kelas yang merepresentasikan sebuah restoran."""

class Restoran:
    """Kelas yang merepresentasikan sebuah restoran."""

    def __init__(self, nama, jenis_masakan):
        """Menginisialisasi restoran."""
        self.nama = nama.title()
        self.jenis_masakan = jenis_masakan
        self.jumlah_pelanggan_dilayani = 0

    def deskripsikan_restoran(self):
        """Menampilkan ringkasan restoran."""
        pesan = f"{self.nama} menyajikan masakan {self.jenis_masakan} yang lezat."
        print(f"\n{pesan}")

    def buka_restoran(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        pesan = f"{self.nama} sedang buka. Silakan mampir!"
        print(f"\n{pesan}")

    def atur_jumlah_pelanggan(self, jumlah_pelanggan):
        """Mengatur jumlah pelanggan yang telah dilayani."""
        self.jumlah_pelanggan_dilayani = jumlah_pelanggan

    def tambah_jumlah_pelanggan(self, tambahan_pelanggan):
        """Menambahkan jumlah pelanggan yang telah dilayani."""
        self.jumlah_pelanggan_dilayani += tambahan_pelanggan