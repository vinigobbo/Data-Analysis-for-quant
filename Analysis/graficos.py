import matplotlib.pyplot as plt
import yfinance as yf

dados = yf.download("VALE3.SA", start="2025-01-01", end="2026-12-31")
fechamento = dados["Close"]
retornos = fechamento.pct_change() * 100

data_maior = retornos.idxmax() .item()
data_menor = retornos.idxmin() .item()

maior = retornos.max() .item()
menor = retornos.min() .item()

print("Maior retorno:", round(maior, 2), "% em", data_maior.date())
print("Menor retorno:", round(menor, 2), "% em", data_menor.date())

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(fechamento)
ax1.set_title("VALE3 - Fechamento")
ax1.set_ylabel("Preço (R$)")

ax2.plot(retornos)
ax2.set_title("VALE3 - Retorno diário (%)")
ax2.set_ylabel("Retorno (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
