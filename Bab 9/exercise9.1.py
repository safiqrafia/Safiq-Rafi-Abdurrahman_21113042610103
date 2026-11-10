class Restoran:
    """Kelas yang merepresentasikan sebuah restoran."""

    def __init__(self, nama, jenis_masakan):
        """Menginisialisasi restoran."""
        self.nama = nama.title()
        self.jenis_masakan = jenis_masakan

    def deskripsikan_restoran(self):
        """Menampilkan ringkasan restoran."""
        pesan = f"{self.nama} menyajikan masakan {self.jenis_masakan} yang lezat."
        print(f"\n{pesan}")

    def buka_restoran(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        pesan = f"{self.nama} sedang buka. Silakan mampir!"
        print(f"\n{pesan}")


restoran = Restoran('Domino', 'Pizza')
print(restoran.nama)
print(restoran.jenis_masakan)

restoran.deskripsikan_restoran()
restoran.buka_restoran()