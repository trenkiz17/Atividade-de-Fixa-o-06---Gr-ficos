"""Gráfico de frequência: quantidade de chamados por tipo de atendimento."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

RAIZ = Path(__file__).resolve().parent.parent
sns.set_theme(style="whitegrid", context="talk")

df = pd.read_csv(RAIZ / "dados" / "dados_frequencia.csv")
freq = df["tipo_atendimento"].value_counts().reset_index()
freq.columns = ["tipo_atendimento", "frequencia"]
total = freq["frequencia"].sum()

fig, ax = plt.subplots(figsize=(11, 7))
sns.barplot(data=freq, x="tipo_atendimento", y="frequencia",
            hue="tipo_atendimento", palette="viridis", legend=False, ax=ax)

for barra, valor in zip(ax.patches, freq["frequencia"]):
    ax.annotate(f"{valor} ({valor / total:.1%})",
                (barra.get_x() + barra.get_width() / 2, barra.get_height()),
                ha="center", va="bottom", fontsize=11, xytext=(0, 4),
                textcoords="offset points")

ax.set_title("Frequência de chamados por tipo de atendimento", fontweight="bold")
ax.set_xlabel("Tipo de atendimento")
ax.set_ylabel("Número de chamados")
ax.set_ylim(0, freq["frequencia"].max() * 1.15)
sns.despine()

fig.tight_layout()
saida = RAIZ / "graficos" / "frequencia.png"
fig.savefig(saida, dpi=150)
print(f"Gráfico salvo em {saida}")
