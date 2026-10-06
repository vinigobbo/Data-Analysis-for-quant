import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np

dados = yf.download("NVDA", start="2025-01-01", end="2026-01-01")
fechamento = dados["Close"].squeeze()
retornos = fechamento.pct_change() * 100

media = retornos.mean()
volatilidade = retornos.std()
vol_anual = retornos.std() * (252 ** 0.5)
data_maior = retornos.idxmax()
data_menor = retornos.idxmin()
maior = retornos.max()
menor = retornos.min()
media = retornos.mean() .item()
volatilidade = retornos.std() .item()
data_maior = retornos.idxmax() .item()
data_menor = retornos.idxmin() .item()
maior = retornos.max() .item()
menor = retornos.min() .item()


print("Volatilidade:", round(volatilidade, 2), "%")
print("Volatilidade anual:", round(vol_anual, 2), "%")
print("Media:", round(media, 2), "%")
print("Maior retorno:", round(maior, 2), "% em", data_maior.date())
print("Menor retorno:", round(menor, 2), "% em", data_menor.date())

media_movel = fechamento.rolling(20).mean()
print(media_movel)

media_movel2 = fechamento.rolling(50).mean()
print(media_movel2)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(fechamento, label="Preço")
ax1.plot(media_movel, label="Média móvel 20 dias")
ax1.plot(media_movel2, label="Média móvel 50 dias")
ax1.legend()
ax1.set_title("NVDA - Fechamento")
ax1.set_ylabel("Preço (US$)")

ax2.plot(retornos, label="Retorno")
ax2.legend()
ax2.set_title("NVDA - Retorno diário (%)")
ax2.set_ylabel("Retorno (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
