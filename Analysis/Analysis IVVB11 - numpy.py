import numpy as np
etf = np.array([443.90, 440.60, 442.50, 443.66, 444.30, 445.61, 448.06])

hoje = etf[1:]
ontem = etf [:-1]

retorno = hoje / ontem - 1
retorno = retorno * 100
print("Retornos:", np.round(retorno, 2))

retorno_max = np.max(retorno)
retorno_min = np.min(retorno)
print("Maior retorno:", np.round(retorno_max, 2), "%")
print("Menor retorno:", np.round(retorno_min, 2), "%")

dias_alta = np.sum(retorno > 0)
print("Dias de alta:", np.round(dias_alta))

media = retorno.mean()
volatilidade = retorno.std() 
print("Media:", np.round(media, 2), "%")
print("Volatilidade:", np.round(volatilidade, 2), "%")