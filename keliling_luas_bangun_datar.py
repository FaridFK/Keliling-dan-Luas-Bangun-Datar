#FUNGSI BANGUN DATAR
def LuasPersegi(sisi):
    luasP = sisi*sisi
    return luasP
def KelilingPersegi(sisi):
    kelilingP  = 4 * sisi
    return kelilingP
def LuasPersegiPanjang(panjang, lebar):
    luasPP = panjang * lebar
    return luasPP
def KelilingPersegiPanjang(panjang, lebar):
    kelilingPP = panjang + panjang + lebar + lebar
    return kelilingPP
def LuasSegitiga(alas,tinggi):
    luasS = 0.5 * alas * tinggi
    return luasS
def KelilingSegitiga(sisiA, sisiB, sisiC):
    kelilingS = sisiA + sisiB + sisiC
    return kelilingS
def LuasLingkaran(r):
    luasL = 3.14 * r * r
    return luasL
def KelilingLingkaran(d):
    kelilingL = 3,14 * d
    return kelilingL 
def LuasJajarGenjang(alas,tinggi):
    luasJG = alas * tinggi
    return luasJG
def KelilingJajarGenjang(sisiA,sisiB):
    kelilingJG = sisiA * 2 + sisiB * 2
    return kelilingJG

#PROGRAM UTAMA
print("==================================== Media Perhitungan Luas & Keliling Bangun Datar ====================================")
print('')
print('')
pilihan = 1
while pilihan != 0:
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Segitiga")
    print("6. Keliling Segitiga")
    print("7. Luas Lingkaran")
    print("8. Keliling Lingkaran")
    print("9. Luas Jajar Genjang")
    print("10. Keliling Jajar Genjang")
    print("0. Exit")
    print('')

    pilihan = int(input("Masukkan Pilihan anda : "))
    print('')
    print('')
    print('')

    if pilihan == 1:
        print("==================================== Luas Persegi ====================================")
        print('')
        sisi = float(input("Masukkan Sisi : "))
        print('')
        print('')
        print("Luas Persegi Adalah ", LuasPersegi(sisi))
        print('')
        print('')
    if pilihan == 2:
        print("==================================== Keliling Persegi ====================================")
        print('')
        sisi = float(input("Masukkan Sisi : "))
        print('')
        print('')
        print("Keliling Persegi Adalah  ", KelilingPersegi(sisi))
        print('')
        print('')
    if pilihan == 3:
        print("==================================== Luas Persegi Panjang ====================================")
        print('')
        panjang = float(input("Masukkan Panjang : "))
        lebar = float(input("Masukkan Lebar : "))
        print('')
        print('')
        print("Luas Persegi Panjang Adalah  ", LuasPersegiPanjang(panjang,lebar))
        print('')
        print('')
    if pilihan == 4:
        print("==================================== Keliling Persegi Panjang ====================================")
        print('')
        panjang = float(input("Masukkan Panjang : "))
        lebar = float(input("Masukkan Lebar : "))
        print('')
        print('')
        print("Keliling Persegi Panjang Adalah  ", KelilingPersegiPanjang(panjang,lebar))
        print('')
        print('')
    if pilihan == 5:
        print("==================================== Luas Segitiga ====================================")
        print('')
        alas = float(input("Masukkan Alas : "))
        tinggi = float(input("Masukkan Tinggi : "))
        print('')
        print('')
        print("Luas Segitiga Adalah ", LuasSegitiga(alas,tinggi))
        print('')
        print('')
    if pilihan == 6:
        print("==================================== Keliling Segitiga ====================================")
        print('')
        sisiA = float(input("Masukkan Sisi A : "))
        sisiB = float(input("Masukkan Sisi B : "))
        sisiC = float(input("Masukkan Sisi C : "))
        print('')
        print('')
        print("Keliling Segitiga Adalah ", KelilingSegitiga(sisiA,sisiB,sisiC))
        print('')
        print('')
    if pilihan == 7:
        print("==================================== Luas Lingkaran ====================================")
        print('')
        r = float(input("Masukkan Jari - Jari : "))
        print('')
        print('')
        print("Luas Lingkaran Adalah  ", LuasLingkaran(r))
        print('')
        print('')
    if pilihan == 8:
        print("==================================== Keliling Lingkaran ====================================")
        print('')
        d = float(input("Masukkan Diameter : "))
        print('')
        print('')
        print("Keliling Lingkaran Adalah ", KelilingLingkaran(d))
        print('')
        print('')
    if pilihan == 9:
        print("==================================== Luas Jarjar Genjang ====================================")
        print('')
        alas = float(input("Masukkan Alas : "))
        tinggi = float(input("Masukkan Tinggi : "))
        print('')
        print('')
        print("Luas Jajar Genjang Adalah : ", LuasJajarGenjang(alas,tinggi))
        print('')
        print('')
    if pilihan == 10:
        print("==================================== Keliling Jajar Genjang ====================================")
        print('')
        sisiA = float(input("Masukkan Sisi A : "))
        sisiB = float(input("Masukkan Sisi B : "))
        print('')
        print('')
        print("Keliling Jajar Genjang Adalah ", KelilingJajarGenjang(sisiA,sisiB))
        print('')
        print('')
