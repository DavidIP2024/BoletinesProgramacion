efectivo = [['2', [50,4],[20,5],[0.5, 6]],
         ['1', [20,15], [10,5], [0.2, 5]],
         ['3',[20,12], [5, 6], [0.02, 5]]]

def mostrarContidoUnhaCaixa(caixa, totalEfectivoCaixas):

    for contidoCaixa in totalEfectivoCaixas:
        if contidoCaixa[0] == caixa:
            print('0 contido da', caixa, "é:")

    mostrarContidoUnhaCaixa('1', efectivo)