# Script para analizar abandono de cliente
# todo por desarrollar

df["segmento_valor"] = pd.qcut(df["valor"], 3, labels=["bajo","medio", "alto"])

