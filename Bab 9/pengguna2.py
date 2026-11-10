"""Kelas untuk merepresentasikan pengguna."""

class Pengguna:
    """Merepresentasikan profil pengguna sederhana."""

    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        """Menginisialisasi pengguna."""
        self.nama_depan = nama_depan.title()
        self.nama_belakang = nama_belakang.title()
        self.nama_pengguna = nama_pengguna
        self.email = email
        self.lokasi = lokasi.title()
        self.percobaan_login = 0

    def deskripsikan_pengguna(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\n{self.nama_depan} {self.nama_belakang}")
        print(f"  Nama Pengguna: {self.nama_pengguna}")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.lokasi}")

    def sapa_pengguna(self):
        """Menampilkan salam khusus kepada pengguna."""
        print(f"\nSelamat datang kembali, {self.nama_pengguna}!")

    def tambah_percobaan_login(self):
        """Menambahkan jumlah percobaan login."""
        self.percobaan_login += 1

    def reset_percobaan_login(self):
        """Mengatur ulang jumlah percobaan login menjadi 0."""
        self.percobaan_login = 0