print("Wahyudi Malihi_E1E120099".center(80,"*"))
def tsukamoto(permintaan, persediaan):
    # Fungsi keanggotaan untuk permintaan
    def permintaan_rendah(x): return max(0, min(1, (800 - x) / 400))
    def permintaan_sedang(x): return max(0, min(1, (x - 800) / 400))
    def permintaan_tinggi(x): return max(0, min(1, (x - 1200) / 400))

    # Fungsi keanggotaan untuk produksi
    def produksi_rendah(x): return max(0, min(1, (2000 - x) / 1000))
    def produksi_sedang(x): return max(0, min(1, (x - 2000) / 1000))
    def produksi_tinggi(x): return max(0, min(1, (x - 3000) / 1000))

    # Aturan fuzzy
    rules = []
    rules.append(min(permintaan_rendah(permintaan), produksi_tinggi(persediaan)))
    rules.append(min(permintaan_sedang(permintaan), produksi_sedang(persediaan)))
    rules.append(min(permintaan_tinggi(permintaan), produksi_rendah(persediaan)))
    rules.append(min(permintaan_sedang(permintaan), produksi_tinggi(persediaan)))

    # Defuzzifikasi dengan metode Tsukamoto
    defuzz = (rules[0] * 3000 + rules[1] * 2000 + rules[2] * 1000 + rules[3] * 2500) / (rules[0] + rules[1] + rules[2] + rules[3])
    w_total = rules[0] + rules[1] + rules[2] + rules[3]
    if w_total == 0:
        return 0
    else:
        return defuzz / w_total

# Contoh penggunaan
produksi = tsukamoto(9900, 500)
print("Jumlah produksi yang direkomendasikan:", produksi, "kemasan")
