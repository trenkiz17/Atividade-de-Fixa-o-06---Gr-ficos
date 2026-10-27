"""Boxplot: distribuição salarial por departamento."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(RAIZ / "dados" / "dados_boxplot.csv")
ordem = df.groupby("departamento")["salario"].median().sort_values(ascending=False).index

fig, ax = plt.subplots(figsize=(11, 7))
sns.boxplot(data=df, x="departamento", y="salario", order=ordem,
            palette="Set2", hue="departamento", legend=False, showfliers=False, ax=ax)
sns.stripplot(data=df, x="departamento", y="salario", order=ordem,
              color="black", alpha=0.35, size=3, ax=ax)

ax.set_title("Distribuição salarial por departamento", fontweight="bold")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário (R$)")
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", ".")))
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "boxplot.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
