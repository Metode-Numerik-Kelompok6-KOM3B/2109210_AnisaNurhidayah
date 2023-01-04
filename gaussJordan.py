# Import library numpy
import numpy as np
import sys

# Membaca nilai dimensi matriks yang diinginkan
n = int(input('Masukan angka untuk n matriks: '))

# Membuat array dengan numpy dari angka x angka increament dan melakukan inisilaisasi ke matriks yang elemennya berisi 0
matriksA = np.zeros((n,n+1))

# Membuat array dengan numpy dari besarnya angka dan melakukan inisialisasi ke angka 0 untuk tempat solusi dalam bentuk vektor
matriksHasil = np.zeros(n)

# Membaca koefisien penjumlahan matriks
print('Masukan Nilai Koefisien Penjumlahan Matriks:')
for i in range(n):
    for j in range(n+1):
        matriksA[i][j] = float(input( 'matriksA['+str(i)+']['+ str(j)+']='))

# Melakukan Implementasi elminasi Gauss-Jordan
for i in range(n):
    if matriksA[i][i] == 0.0:
        sys.exit('Mendeteksi Pembagian dengan 0!')
        
    for j in range(n):
        if i != j:
            ratio = matriksA[j][i]/matriksA[i][i]

            for k in range(n+1):
                matriksA[j][k] = matriksA[j][k] - ratio * matriksA[i][k]


for i in range(n):
    matriksHasil[i] = matriksA[i][n]/matriksA[i][i]

# Menampilkan solusi
print('\nSolusi  : ')
for i in range(n):
    print('X%d = %0.2f' %(i,matriksHasil[i]), end = '\t')