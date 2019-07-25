def contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva):
    for i in range(len(minhaLista)):
        if i > 0 and minhaLista[i] > minhaLista[i - 1]:
            for j in range(minhaLista[i - 1], minhaLista[i]):
                volumeDeChuva = volumeDeChuva + mapeamento[j]
                mapeamento[j] = 0
        if i > 0 and minhaLista[i] < maiorAlturaAlcancada:
            for j in range(minhaLista[i], maiorAlturaAlcancada):
                mapeamento[j] = mapeamento[j] + 1
        if minhaLista[i] > maiorAlturaAlcancada:
            maiorAlturaAlcancada = minhaLista[i]
    return volumeDeChuva