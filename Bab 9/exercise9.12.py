from admin import Administrator

cristiano_ronaldo = Administrator(
    'cristiano',
    'ronaldo',
    'cr7',
    'cr7@example.com',
    'riyadh'
)

cristiano_ronaldo.deskripsikan_pengguna()

hak_akses_ronaldo = [
    'dapat menambahkan postingan',
    'dapat menghapus postingan',
    'dapat memblokir pengguna',
    'dapat mengatur ulang kata sandi',
]

cristiano_ronaldo.hak_akses.hak_akses = hak_akses_ronaldo

print(
    f"\nAdministrator {cristiano_ronaldo.nama_pengguna} "
    "memiliki hak akses berikut:"
)

cristiano_ronaldo.hak_akses.tampilkan_hak_akses()