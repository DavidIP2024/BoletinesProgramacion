n = int(input("Dime un número entre 1 y 99:"))
p = ["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve","diez"]
s = ["","once","doce","trece","catorce","quize","dieciseis","diecisiete","dieciocho","dicinueve"]
f = ["","","veinte","trenta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
if n > 0 and n < 11:
    print(p[n])
elif n >= 11 and n < 20:
    r = n-10
    print(s[r])
elif n >=20 and n < 100:
    r1 =  n//10
    r2 = n%10
    print(f[r1], "y", p[r2])