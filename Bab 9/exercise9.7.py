class Pengguna:
    """Merepresentasikan profil pengguna sederhana."""

    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        """Menginisialisasi pengguna."""
        self.nama_depan = nama_depan.title()
        self.nama_belakang = nama_belakang.title()
        self.nama_pengguna = nama_pengguna
        self.email = email
        self.lokasi = lokasi.title()

    def deskripsikan_pengguna(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"\n{self.nama_depan} {self.nama_belakang}")
        print(f"  Nama Pengguna: {self.nama_pengguna}")
        print(f"  Email: {self.email}")
        print(f"  Lokasi: {self.lokasi}")


class Administrator(Pengguna):
    """Pengguna yang memiliki hak akses administratif."""

    def __init__(self, nama_depan, nama_belakang, nama_pengguna, email, lokasi):
        """Menginisialisasi administrator."""
        super().__init__(nama_depan, nama_belakang, nama_pengguna, email, lokasi)
        self.hak_akses = []

    def tampilkan_hak_akses(self):
        """Menampilkan daftar hak akses administrator."""
        print("\nHak Akses Administrator:")
        for hak in self.hak_akses:
            print(f"- {hak}")


cristiano_ronaldo = Administrator(
    'cristiano',
    'ronaldo',
    'cr7',
    'cr7@example.com',
    'riyadh'
)

cristiano_ronaldo.deskripsikan_pengguna()

cristiano_ronaldo.hak_akses = [
    'dapat menambahkan postingan',
    'dapat menghapus postingan',
    'dapat memblokir pengguna',
    'dapat mengatur ulang kata sandi',
]

cristiano_ronaldo.tampilkan_hak_akses()
