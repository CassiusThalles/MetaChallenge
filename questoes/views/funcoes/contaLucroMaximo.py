def contaLucroMaximo(variacaoDeValor, contador, lucroMaximo):
    for i in range(len(variacaoDeValor)):
        if contador + variacaoDeValor[i] >= contador:
            contador = contador + variacaoDeValor[i]
        if contador + variacaoDeValor[i] < contador:
            if contador + variacaoDeValor[i] > 0:
                contador = contador + variacaoDeValor[i]
            else:
                contador = 0
        if contador > lucroMaximo:
            lucroMaximo = contador
    return lucroMaximo