"""Regressão linear: gasto mensal em função da renda mensal."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

from scipy import stats

df = pd.read_csv(RAIZ / "dados" / "dados_regressao.csv")
res = stats.linregress(df["renda_mensal"], df["gasto_mensal"])

fig, ax = plt.subplots(figsize=(11, 7))
sns.regplot(data=df, x="renda_mensal", y="gasto_mensal", ci=95,
            scatter_kws={"alpha": 0.6, "s": 55},
            line_kws={"color": "crimson", "linewidth": 2.5}, ax=ax)

texto = (f"gasto = {res.slope:.3f} × renda + {res.intercept:.1f}\n"
         f"R² = {res.rvalue ** 2:.3f}")
ax.text(0.04, 0.95, texto, transform=ax.transAxes, va="top", fontsize=13,
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.9})

ax.set_title("Regressão linear: gasto mensal × renda mensal", fontweight="bold")
ax.set_xlabel("Renda mensal (R$)")
ax.set_ylabel("Gasto mensal (R$)")
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "regressao.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
