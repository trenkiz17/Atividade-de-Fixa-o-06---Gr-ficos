"""Gráfico de dispersão: altura x peso, colorido por sexo."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(RAIZ / "dados" / "dados_dispersao.csv")

fig, ax = plt.subplots(figsize=(11, 7))
sns.scatterplot(data=df, x="altura_cm", y="peso_kg", hue="sexo",
                style="sexo", s=90, alpha=0.8, palette="Set1", ax=ax)

ax.set_title("Relação entre altura e peso", fontweight="bold")
ax.set_xlabel("Altura (cm)")
ax.set_ylabel("Peso (kg)")
ax.legend(title="Sexo", frameon=False)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "dispersao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
