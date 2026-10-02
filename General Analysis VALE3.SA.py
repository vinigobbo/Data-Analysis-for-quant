import yfinance as yf
import numpy as np

dados = yf.download("VALE3.SA", start="2026-01-01", end="2026-09-30")
fechamento = dados["Close"]

retornos = fechamento.pct_change()

media = retornos.mean().item()
volatilidade = retornos.std().item()

print("Media: ", round(media * 100, 2), "%")
print("Volatilidade", round(volatilidade * 100, 2), "%")

retorno_max = np.max(retornos).item()
retorno_min = np.min(retornos).item()
print("Retorno maximo: ", round(retorno_max * 100, 2), "%")
print("Retorno minimo: ", round(retorno_min * 100, 2), "%")

dias_alta = np.sum(retornos > 0)
dias_queda = np.sum(retornos < 0)

print("Dias de alta: ", dias_alta)
print("Dias de queda: ", dias_queda)

volume = dados["Volume"]
media_volume = volume.mean().item()
print("Volume medio: ", round(media_volume))
