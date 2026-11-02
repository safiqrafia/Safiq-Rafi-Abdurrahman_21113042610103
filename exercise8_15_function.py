
def cetak_model(desain_belum_dicetak, model_selesai):
    """Mensimulasikan proses mencetak setiap desain."""
    while desain_belum_dicetak:
        desain_sekarang = desain_belum_dicetak.pop()
        print(f"Mencetak model: {desain_sekarang}")
        model_selesai.append(desain_sekarang)


def tampilkan_model_selesai(model_selesai):
    """Menampilkan semua model yang sudah dicetak."""
    print("\nModel berikut telah selesai dicetak:")
    for model in model_selesai:
        print(model)