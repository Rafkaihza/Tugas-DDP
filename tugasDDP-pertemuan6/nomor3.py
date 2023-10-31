jbaris = int(input("Masukkan jumlah baris: "))

for baris in range(1, jbaris + 1):
    for kolom in range(baris):
        print("*", end="")
    print() 
