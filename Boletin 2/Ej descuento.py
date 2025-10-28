precioTarifa = int(input('Introduce el precio de la tarifa: '))
precioPagado = int(input('Introduce el precio pagado: '))
descuento = ((precioTarifa - precioPagado)/precioTarifa) * 30
print('El descuento es de: ',descuento,'%')