soldo_fixo = float(input("Introduce o soldo fixo (€): "))
vendas = float(input("Introduce o importe total das vendas (€): "))
quilometros = float(input("Introduce os quilómetros percorridos: "))
dias_desprazamento = int(input("Introduce os días de desprazamento: "))

comision = vendas * 0.05
quilometraxe = quilometros * 2
dietas = dias_desprazamento * 30

soldo_bruto = soldo_fixo + comision + quilometraxe + dietas

irpf = soldo_bruto * 0.18
seguridade_social = 36

soldo_liquido = soldo_bruto - irpf - seguridade_social

print('Soldo bruto: ',soldo_bruto)
print('Soldo líquido: ', soldo_liquido)