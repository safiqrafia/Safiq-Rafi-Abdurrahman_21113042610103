class Mobil:
    """Merepresentasikan sebuah mobil."""

    def __init__(self, merek, model, tahun):
        """Menginisialisasi atribut untuk mendeskripsikan mobil."""
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.pembacaan_odometer = 0

    def dapatkan_nama_lengkap(self):
        """Mengembalikan nama mobil dengan format yang rapi."""
        nama_lengkap = f"{self.tahun} {self.merek} {self.model}"
        return nama_lengkap.title()

    def baca_odometer(self):
        """Menampilkan jarak tempuh mobil."""
        print(f"Mobil ini telah menempuh {self.pembacaan_odometer} kilometer.")

    def perbarui_odometer(self, jarak_tempuh):
        """Mengatur pembacaan odometer sesuai nilai yang diberikan."""
        if jarak_tempuh >= self.pembacaan_odometer:
            self.pembacaan_odometer = jarak_tempuh
        else:
            print("Odometer tidak dapat dikurangi!")

    def tambah_odometer(self, kilometer):
        """Menambahkan jarak tempuh pada odometer."""
        self.pembacaan_odometer += kilometer


class Baterai:
    """Merepresentasikan baterai pada mobil listrik."""

    def __init__(self, kapasitas_baterai=40):
        """Menginisialisasi atribut baterai."""
        self.kapasitas_baterai = kapasitas_baterai

    def deskripsikan_baterai(self):
        """Menampilkan informasi kapasitas baterai."""
        print(f"Mobil ini memiliki baterai berkapasitas {self.kapasitas_baterai} kWh.")

    def dapatkan_jarak_tempuh(self):
        """Menampilkan jarak tempuh berdasarkan kapasitas baterai."""
        if self.kapasitas_baterai == 40:
            jarak_tempuh = 150
        elif self.kapasitas_baterai == 65:
            jarak_tempuh = 225

        print(f"Mobil ini dapat menempuh sekitar {jarak_tempuh} kilometer dengan baterai penuh.")

    def tingkatkan_baterai(self):
        """Meningkatkan kapasitas baterai jika memungkinkan."""
        if self.kapasitas_baterai == 40:
            self.kapasitas_baterai = 65
            print("Kapasitas baterai berhasil ditingkatkan menjadi 65 kWh.")
        else:
            print("Kapasitas baterai sudah ditingkatkan.")


class MobilListrik(Mobil):
    """Merepresentasikan mobil khusus kendaraan listrik."""

    def __init__(self, merek, model, tahun):
        """
        Menginisialisasi atribut dari kelas induk.
        Kemudian menginisialisasi atribut khusus mobil listrik.
        """
        super().__init__(merek, model, tahun)
        self.baterai = Baterai()


print("Membuat mobil listrik dan memeriksa jarak tempuh:")
mobil_saya = MobilListrik('hyundai', 'ioniq 5', 2024)
mobil_saya.baterai.dapatkan_jarak_tempuh()

print("\nMeningkatkan kapasitas baterai dan memeriksa jarak tempuh kembali:")
mobil_saya.baterai.tingkatkan_baterai()
mobil_saya.baterai.dapatkan_jarak_tempuh()