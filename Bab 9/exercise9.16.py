from random import choice

daftar_peserta = [
    'Cristiano Ronaldo',
    'Lionel Messi',
    'Kylian Mbappe',
    'Neymar Jr',
    'Erling Haaland'
]

pemenang = choice(daftar_peserta)

print("Daftar Peserta:")
for peserta in daftar_peserta:
    print(f"- {peserta}")

print(f"\nPemenang undian adalah: {pemenang}")