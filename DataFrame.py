import pandas as pd
datas = pd.date_range("2026-09-24", periods=3)
dados = {
    "Fechamento": [443.90, 440.60, 442.50],
    "Volume": [12000, 9800, 15400]
}
df = pd.DataFrame(dados, index=datas)
retornos = df["Fechamento"].pct_change()
print(retornos)

media = retornos.mean()
volatilidade = retornos.std()

print(round(media * 100, 2), "%")
print(round(volatilidade * 100, 2), "%")