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


ratu_rasa = Restoran('ratu rasa', 'masakan nusantara')
ratu_rasa.deskripsikan_restoran()

dapur_nusantara = Restoran('dapur nusantara', 'masakan tradisional')
dapur_nusantara.deskripsikan_restoran()

pondok_pedas = Restoran('pondok pedas', 'masakan pedas')
pondok_pedas.deskripsikan_restoran()