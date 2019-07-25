def balanceada(sequencia: list):
    valorauxiliar = len(sequencia) / 2
    valorauxiliar = int(valorauxiliar)
    resposta = "SIM"
    for i in reversed(range(valorauxiliar)):
        if (sequencia[i] == "("):
            if (sequencia[2 * valorauxiliar - i - 1] != ")"):
                resposta = "NÃO"
                break
        if (sequencia[i] == "["):
            if (sequencia[2 * valorauxiliar - i - 1] != "]"):
                resposta = "NÃO"
                break
        if (sequencia[i] == "{"):
            if (sequencia[2 * valorauxiliar - i - 1] != "}"):
                resposta = "NÃO"
                break
    return resposta