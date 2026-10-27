"""Gráfico de linhas: evolução diária das vendas por loja."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

import matplotlib.dates as mdates

df = pd.read_csv(RAIZ / "dados" / "dados_linhas.csv", parse_dates=["data"])
df = df.sort_values("data")
ordem_lojas = sorted(df["loja"].unique())

fig, ax = plt.subplots(figsize=(13, 7))
sns.lineplot(data=df, x="data", y="vendas", hue="loja", hue_order=ordem_lojas, marker="o",
             markersize=6, linewidth=1.8, palette="Set1", ax=ax)

ax.set_title("Evolução diária das vendas por loja (1º trimestre de 2026)",
             fontweight="bold")
ax.set_xlabel("Data")
ax.set_ylabel("Vendas")
ax.xaxis.set_major_locator(mdates.MonthLocator())
MESES = ["jan", "fev", "mar", "abr", "mai", "jun",
         "jul", "ago", "set", "out", "nov", "dez"]
ax.xaxis.set_major_formatter(plt.FuncFormatter(
    lambda v, _: (lambda d: f"{MESES[d.month - 1]}/{d.year}")(mdates.num2date(v))))
ax.legend(title="Loja", frameon=False)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "linhas.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
