unidades = ["", "un", "dous", "tres", "catro", "cinco", "seis", "sete", "oito", "nove"]
decenas = ["", "dez", "vinte", "trinta", "corenta", "cincuenta", "sesenta", "setenta", "oitenta", "noventa"]

num = int(input("Introduce un número entre 1 e 99: "))
while num < 1 or num > 99:
    print("Número incorrecto. Ten que ser entre 1 e 99.")
    num = int(input("Introduce un número entre 1 e 99: "))

if num < 10:
    print(unidades[num])
else:
    dec = num // 10
    uni = num % 10
    if uni == 0:
        print(decenas[dec])
    else:
        print(decenas[dec], "e", unidades[uni])