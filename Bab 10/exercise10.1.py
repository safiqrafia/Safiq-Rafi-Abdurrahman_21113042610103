from pathlib import Path

print("--- Membaca seluruh isi file:")
path = Path('learning_python.txt')
isi_file = path.read_text()
print(isi_file)

print("\n--- Membaca file baris demi baris:")
baris = isi_file.splitlines()
for baris_teks in baris:
    print(baris_teks)