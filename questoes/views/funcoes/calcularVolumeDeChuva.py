from questoes.views.funcoes import contaVolumeDeChuva

def calcularVolumeDeChuva(minhaLista):
    maiorAltura = max(minhaLista)
    mapeamento = [0] * maiorAltura
    maiorAlturaAlcancada = 0
    volumeDeChuva = 0
    volumeDeChuva = contaVolumeDeChuva.contaVolumeDeChuva(minhaLista, mapeamento, maiorAlturaAlcancada, volumeDeChuva)
    return volumeDeChuva
