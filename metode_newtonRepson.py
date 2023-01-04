#Mencari akar dengan metode newton rephson
#definisikan fungsi
def f(x):
    return x**3-5*x-9

#definisikan turunan dari fungsi
def g(x):
    return 3*x**2 -6

# Implementasi Metode Newton Raphson
def newtonRaphson(x0,e,N):
    step = 1
    flag = 1
    condition = True
    #jika turunan fungsinya adalah 0 maka akan terjadi error karena dibagi dengan 0
    while condition:
        if g(x0) == 0.0:
            print('Error karena dibagi dengan 0')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    #jika flagnya hanya 1 maka akar adalah nilai dari x1
    if flag==1:
        print('\nAkarnya adalah: %0.8f' % x1)
    else:
        print('\nTidak Konvergen.')


# Input Section
x0 = input('Masukkan tebakan: ')
e = input('Galat: ')
N = input('Banyak step: ')

# Mengkonversi nilai x0 dan e ke float
x0 = float(x0)
e = float(e)

# Mengkonversi nilai N ke integer
N = int(N)

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)