# Mencari integral untuk f(x) dengan metode trapesium
e= 2.71828                  #dideklarasikan dan digunakan apabila inputan mengandung e
def f(x):
    z = eval(fx)            # eval digunakan untuk mengubah dari string menjadi fungsi yang dapat dioperasikan
    return z                # mengembalikkan nilai z atau fungsi inputan user

# Algoritma Trapesium
def trapezoidal(a,b,n):
    h = (b - a) / n                  # mencari h atau lebar segemen
    integration = f(a) + f(b)        # menjumlahkan fungsi dari batas bawah dan batas bawah
    for i in range(1,n):            
        k = a + i*h                  # menentukan nilai titik selanjutnya
        integration = integration + 2 * f(k)   
    integration = integration * h/2
    return integration               # mengembalikan nilai integral
    
# Input
fx = str(input("Masukkan fungsi integral : "))
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))
n = int(input("Masukkan jumlah iterasi: "))

# Menampilkan Hasil
result = trapezoidal(a, b, n)
print("Integral dengan metode trapesium: %0.6f" % (result))# Mencari integral untuk f(x) dengan metode trapesium