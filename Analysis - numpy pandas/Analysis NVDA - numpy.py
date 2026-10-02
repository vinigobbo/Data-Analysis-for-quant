import numpy as np
etf = np.array([218.29, 210.96, 212.17, 213.90, 219.34, 222.27, 227.38, 228.87, 225.51, 224.58, 225.04, 230.30])

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