#Mencari akar dengan metode bagi dua
# Mendefinisikan fungsi
def f(x):
    return x**3-5*x-9

# Implementasi Metode Bagi Dua
def bagiDua(a,b,galat):
    i = 1
    kondisi = True
    while kondisi:
        c = (a + b)/2
        print('Iterasi ke-%d, c = %0.6f dan f(c) = %0.6f' % (i, c, f(c)))
        #jika f(a)*f(c)kurang dari 0 maka nilai b=c sedangkan jika f(a)*f(b) lebih dari 0 maka nilai a=c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        i += 1
        kondisi = abs(f(c)) > galat

    print('\nAkar yang ditemukan adalah : %0.8f' % c)

#Input
a = input('Masukan Tebakan Pertama: ')
b = input('Masukan Tebakan Kedua: ')
galat = input('Tolerable Kesalahan: ')

# Konversi variabel input ke bentuk double
a = float(a)
b = float(b)
galat = float(galat)


# Proses pengecekan dari nilai tebakan yang telah dimasukan
if f(a) * f(b) > 0.0:
    print('Tebakan yang dimasukan tidak memiliki nilai akar atau memiliki akar kembar.')
    print('Coba lagi dengan nilai tebakan yang berbeda!')
else:
    bagiDua(a,b,galat)