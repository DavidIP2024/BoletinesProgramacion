VentasAnuales = int(input('Introduce el numero de ventas anuales: '))
if VentasAnuales <= 100:
    print('Articulo de consumo bajo')
elif VentasAnuales > 100 and VentasAnuales <= 500:
    print('Aticulo de consumo medio')
elif VentasAnuales >500 and VentasAnuales <= 1000:
    print('Articulo de consumo alto')
elif VentasAnuales > 1000:
    print('Articulo de primera necesidad')
