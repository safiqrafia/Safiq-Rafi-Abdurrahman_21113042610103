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


class KedaiEsKrim(Restoran):
    """Merepresentasikan sebuah kedai es krim."""

    def __init__(self, nama, jenis_masakan='es krim potong'):
        """Menginisialisasi kedai es krim."""
        super().__init__(nama, jenis_masakan)
        self.varian_rasa = []

    def tampilkan_varian_rasa(self):
        """Menampilkan varian rasa yang tersedia."""
        print("\nKami menyediakan varian rasa berikut:")
        for rasa in self.varian_rasa:
            print(f"- {rasa.title()}")


es_krim_potong = KedaiEsKrim('es krim potong')
es_krim_potong.varian_rasa = ['vanila', 'cokelat', 'stroberi']

es_krim_potong.deskripsikan_restoran()
es_krim_potong.tampilkan_varian_rasa()