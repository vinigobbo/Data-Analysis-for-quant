etf = [443.90, 440.60, 442.50, 443.66, 444.30, 445.61, 448.06]
retornos = []
desvios = []
for i in range(1, len(etf)):
  retorno = etf[i] / etf[i - 1] - 1
  retornos.append(round(retorno * 100, 2))
print("Retornos:", retornos)

retorno_max = max(retornos)
retorno_min = min(retornos)
print("Maior retorno:", retorno_max, "%")
print("Menor retorno:", retorno_min, "%")

dias_alta = 0

for retorno in retornos:
  if retorno > 0:
    dias_alta += 1
print("Dias de alta:", dias_alta)

media = sum(retornos) / len(retornos)
print("Media:", round(media, 2), "%")

soma_quadrados = 0

for r in retornos:
  desvio = r - media
  soma_quadrados = soma_quadrados + desvio ** 2
print("Soma dos quadrados:", round(soma_quadrados, 5))

volatilidade = (soma_quadrados / len(retornos)) ** 0.5
print("Volatilidade:", round(volatilidade, 2), "%")