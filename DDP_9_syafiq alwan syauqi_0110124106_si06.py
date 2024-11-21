print('\n--- CELCUIS KE FAHRENHEIT ---')
def celsius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celsius_ke_fahrenheit(0)

print('\n--- MENCARI BILANGAN GENAP ---')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('\n--- KETERANGAN LULUS DAN TIDAK LULUS ---')
def skor(nilai):
    if nilai >= 80:
        print('lulus')
    else:
        print('gagal')
        
skor(80)
skor(60)

print('\n---    MENCETAK BILANGAN GANJIL ---')
def bil_ganjil(ganjil):
    for a in range(1,ganjil+1, 2):
        print(a, end=' ')
bil_ganjil(20)