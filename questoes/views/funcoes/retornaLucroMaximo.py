from questoes.views.funcoes.contaLucroMaximo import contaLucroMaximo

def retornaValorMaximo(input):
    variacaoDeValor = []
    for i in range(1, len(input)):
        valorAuxiliar = input[i] - input[i - 1]
        variacaoDeValor.append(valorAuxiliar)
    lucroMaximo = 0
    contador = 0
    lucroMaximo = contaLucroMaximo(variacaoDeValor, contador, lucroMaximo)
    return lucroMaximo
