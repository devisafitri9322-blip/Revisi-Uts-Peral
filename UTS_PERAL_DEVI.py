def kegiatan_terpilih(kegiatan):
    # Urutkan berdasarkan waktu selesai
    kegiatan.sort(key=lambda x: x[2])

    terpilih = []
    waktu_selesai = 0

    for nama, mulai, selesai in kegiatan:
        if mulai >= waktu_selesai:
            terpilih.append(nama)
            waktu_selesai = selesai

    return terpilih, len(terpilih)

#Inputan jumlah kegiatan dari user
jumlah_kegiatan = int(input("Masukkan jumlah kegiatan: "))
kegiatan = []

for i in range(jumlah_kegiatan):
    nama = input(f"Masukkan nama kegiatan ke-{i+1}: ")
    mulai = int(input(f"Masukkan waktu mulai kegiatan ke-{i+1} (dalam format 24 jam, misal 13 untuk jam 1 siang): "))
    selesai = int(input(f"Masukkan waktu selesai kegiatan ke-{i+1} (dalam format 24 jam, misal 15 untuk jam 3 sore): "))
    kegiatan.append((nama, mulai, selesai))     

terpilih, jumlah = kegiatan_terpilih(kegiatan)

print("Kegiatan yang dipilih:", terpilih)
print("Jumlah kegiatan:", jumlah)
