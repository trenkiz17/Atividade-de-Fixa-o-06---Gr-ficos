"""Gráfico de barras agrupadas: vendas médias por categoria e região."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(RAIZ / "dados" / "dados_barras.csv")

fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(data=df, x="categoria", y="vendas_medias", hue="regiao",
            palette="deep", ax=ax)

for container in ax.containers:
    ax.bar_label(container, fmt="%.0f", padding=3, fontsize=10)

ax.set_title("Vendas médias por categoria e região", fontweight="bold")
ax.set_xlabel("Categoria")
ax.set_ylabel("Vendas médias")
ax.set_ylim(0, df["vendas_medias"].max() * 1.15)
ax.legend(title="Região", frameon=False, loc="upper center",
          bbox_to_anchor=(0.5, -0.17), ncol=4)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "barras.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
