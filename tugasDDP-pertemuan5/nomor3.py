pilihan = input("""Silahkan pilih tools dibawah ini dengan mengirimkan nomornya
===================
tools yang tersedia
===================
1.Menghitung luas persegi (persegi)
2.Menghitung luas lingkaran (lingkaran)
3.Menghitung luas segitiga (segitiga)
===================
pilihan mu?
"""
)

match pilihan :

    case "1" | "persegi" | "Persegi" | "PERSEGI":
        print("kamu memilih menghitung luas persegi")
        sisi = int(input("Masukkan panjang sisi persegi: "))
        luaspersegi = sisi * sisi
        print("Luas persegi dengan panjang sisi", sisi, "adalah", luaspersegi)

    case "2" | "lingkaran" | "Lingkaran" | "LINGKARAN":
        print("kamu memilih menghitung luas lingkaran")
        jari2 = int(input("Masukkan panjang jari-jari lingkaran: "))
        luaslingkaran = 3.14 * jari2 * jari2
        print("Luas lingkaran dengan jari-jari", jari2, "adalah", luaslingkaran)

    case "3" | "segitiga" | "Segitiga" | "SEGITIGA":
        print("kamu memilih menghitung luas segitiga")
        alas = int(input("Masukkan panjang alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        luassegitiga = 0.5 * alas * tinggi
        print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luassegitiga)

    case _:
        print("salah memasukan pilihan")