"""Gráfico de pizza: participação de cada canal no faturamento."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(RAIZ / "dados" / "dados_pizza.csv")
df = df.sort_values("faturamento", ascending=False)

fig, ax = plt.subplots(figsize=(9, 9))
cores = sns.color_palette("pastel", len(df))
ax.pie(df["faturamento"], labels=df["canal_venda"], colors=cores,
       autopct="%1.1f%%", startangle=90, counterclock=False, pctdistance=0.78,
       wedgeprops={"edgecolor": "white", "linewidth": 2},
       textprops={"fontsize": 14})

total = df["faturamento"].sum()
ax.set_title(f"Faturamento por canal de venda\n(total: R$ {total:,.0f})"
             .replace(",", "."), fontweight="bold")
ax.axis("equal")

fig.tight_layout()
saida = RAIZ / "graficos" / "pizza.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
