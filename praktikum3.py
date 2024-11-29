print()
print('=== Profile Ammar Falah Gunawan ===')

nama = ' Ammar Falah Gunawan'
nim = '0110124212'
rombel = 'Si06'
alamat = 'Jakarta,pekayon Pasar Rebo N0 12 a'

print(nama)
print(nim)
print(rombel)
print(alamat)

print('Nama Saya', nama, 'dengan NIM', nim, 'Rombel Saya', rombel, 'tinggal di', alamat)



# Menghitung Berat Badan Ideal
print()
print('===Berat Badan Ideal===')

# Input Perhitungan
tinggi_badan = 175

# Proses Perhitungan
berat_badan_ideal = (tinggi_badan-100)-(tinggi_badan-100)*1/10

# Output Perhitungan
print('Berat badan ideal untuk tinggi', tinggi_badan, 'CM adalah', berat_badan_ideal, 'kg')




# Menghitung Celcius Ke Fahrenheit
print()
print('===Suhu Celcius Ke Fahrenheit===')

# Input Perhitungan
celcius = int(input('Masukan Suhu Celcius: '))

# Proses Perhitungan
rumus_fahrenheit = int(celcius*9/5)+32

# Output Perhitungan
print(celcius, 'Celcius sama dengan', rumus_fahrenheit, 'Fahrenheit')




# Menghitung Luas Tabung
print("")
print("=====Luas Tabung======")

# Input Angka
phi = 3.14
jari2 = int(input('Masukan nilai jari-jari: '))
tinggi = int(input('Masukan nilai tinggi: '))

# Proses Perhitungan
luas_permukaan =  2*phi*jari2*(jari2+tinggi)
luas_alas = phi*jari2**2
luas_selimut = 2 * phi * jari2 * tinggi

# Output Perhitungan
print('Luas Permukaan Tabung Adalah: ', luas_permukaan)
print('Luas Alas Tabung Adalah: ', luas_alas)
print('Luas Selimut Tabung Adalah: ', luas_selimut)

