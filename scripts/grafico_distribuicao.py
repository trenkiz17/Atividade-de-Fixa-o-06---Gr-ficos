"""Histograma com curva de densidade: distribuição de idade dos clientes."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(RAIZ / "dados" / "dados_distribuicao.csv")
media, mediana = df["idade"].mean(), df["idade"].median()

fig, ax = plt.subplots(figsize=(11, 7))
sns.histplot(data=df, x="idade", bins=15, kde=True, color="#4C72B0", ax=ax)
ax.axvline(media, color="crimson", linestyle="--", linewidth=2,
           label=f"Média: {media:.1f} anos")
ax.axvline(mediana, color="darkgreen", linestyle=":", linewidth=2,
           label=f"Mediana: {mediana:.1f} anos")

ax.set_title("Distribuição de idade dos clientes", fontweight="bold")
ax.set_xlabel("Idade (anos)")
ax.set_ylabel("Número de clientes")
ax.legend(frameon=False)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "distribuicao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
