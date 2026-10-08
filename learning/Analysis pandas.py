import pandas as pd

datas = pd.date_range("2026-09-24", periods=7)
precos = pd.Series([455.67, 452.29, 447.37, 451.53, 453.00, 453.00, 451.15], index=datas)
print(precos)
retornos = precos.pct_change ()
print(retornos)

media = retornos.mean()
volatilidade = retornos.std()

print(round(media * 100, 2), "%")
print(round(volatilidade * 100, 2), "%")