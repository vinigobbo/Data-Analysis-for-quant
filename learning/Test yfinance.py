import yfinance as yf

dados = yf.download("PETR4.SA", start="2026-08-01", end="2026-09-30")
fechamento = dados["Close"]

retornos = fechamento.pct_change()

media = retornos.mean()
volatilidade = retornos.std()

print(round(media * 100, 2), "%")
print(round(volatilidade * 100, 2), "%")