def retornaIndices(lista: list, alvo: int):
    mydict = {}
    for i in list(range(len(lista))):
        mydict.update({lista[i]: i})

    for i in list(range(len(lista))):
        diferenca = alvo - lista[i]
        if diferenca in mydict.keys():
            return [i, mydict[diferenca]]

    return [0, 0]