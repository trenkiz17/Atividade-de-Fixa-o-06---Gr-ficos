"""Dashboard Streamlit com os gráficos gerados na atividade anterior.

Execute com:  streamlit run app.py
"""
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# DADOS DO ALUNO  -> edite estas três linhas com as suas informações
# ---------------------------------------------------------------------------
NOME_ALUNO = "Seu Nome Completo"
NUMERO_CHAMADA = "00"
TURMA = "Sua Turma"
# ---------------------------------------------------------------------------

PASTA_GRAFICOS = Path(__file__).resolve().parent / "graficos"

# Cada gráfico: título, arquivo e uma breve análise baseada nos dados do CSV.
GRAFICOS = [
    {
        "titulo": "Vendas médias por categoria e região",
        "arquivo": "barras.png",
        "analise": (
            "A região **Oeste** lidera com média de 225 em vendas, enquanto o "
            "**Norte** tem a menor (102). Entre as categorias, **Livros** se "
            "destaca (média 187). O melhor resultado individual é Livros no "
            "Oeste (284) e o pior, Alimentos no Norte (54)."
        ),
    },
    {
        "titulo": "Evolução diária das vendas por loja",
        "arquivo": "linhas.png",
        "analise": (
            "As vendas mostram **forte tendência de alta** no trimestre: a média "
            "mensal sobe de 122 em janeiro para 225 em março. A Loja B tem média "
            "ligeiramente maior (179 contra 168 da Loja A), mas as duas "
            "caminham juntas e se alternam na liderança."
        ),
    },
    {
        "titulo": "Faturamento por canal de venda",
        "arquivo": "pizza.png",
        "analise": (
            "Do faturamento total de R$ 120 mil, o **Site** responde por 37,5% e "
            "a Loja Física por 26,7%: juntos somam mais de 64%. O Telefone é o "
            "canal menos relevante, com apenas 6,7%."
        ),
    },
    {
        "titulo": "Frequência de chamados por tipo de atendimento",
        "arquivo": "frequencia.png",
        "analise": (
            "**Dúvidas** são o tipo mais comum (38,7% dos 300 chamados), seguidas "
            "por Reclamações (24,3%). Elogios são a minoria (9,7%) e os "
            "Cancelamentos somam 11%, um ponto de atenção para retenção."
        ),
    },
    {
        "titulo": "Distribuição de idade dos clientes",
        "arquivo": "distribuicao.png",
        "analise": (
            "A idade média é 33,6 anos e a mediana 29, o que indica "
            "**assimetria à direita**: há mais clientes jovens, com cauda de "
            "clientes mais velhos. Cerca de 61% têm até 35 anos e só 2% passam "
            "dos 55."
        ),
    },
    {
        "titulo": "Distribuição salarial por departamento",
        "arquivo": "boxplot.png",
        "analise": (
            "**Vendas e TI** pagam bem mais (mediana de R$ 7.130 e R$ 6.614) do "
            "que Marketing e RH (cerca de R$ 4.190). Há outliers de até "
            "R$ 21.000 em TI e Vendas, e de R$ 12.000 em Marketing e RH."
        ),
    },
    {
        "titulo": "Relação entre altura e peso",
        "arquivo": "dispersao.png",
        "analise": (
            "Existe **correlação positiva forte** (r ≈ 0,86): quanto maior a "
            "altura, maior tende a ser o peso. Homens e mulheres da amostra têm "
            "médias muito próximas (cerca de 170 cm e 62–63 kg) e o mesmo grau "
            "de correlação."
        ),
    },
    {
        "titulo": "Regressão linear: gasto × renda",
        "arquivo": "regressao.png",
        "analise": (
            "O modelo tem **R² de 0,98**, ou seja, a renda explica quase toda a "
            "variação do gasto. A cada R$ 1,00 a mais de renda, o gasto "
            "aumenta cerca de R$ 0,57, e em média as pessoas gastam 63% do "
            "que ganham."
        ),
    },
    {
        "titulo": "Movimento de clientes por dia e horário",
        "arquivo": "heatmap.png",
        "analise": (
            "O fim de semana concentra o movimento: **Domingo (836) e Sábado "
            "(776)** são os dias mais cheios, com média de 115 clientes por "
            "horário contra 60 nos dias úteis. O pico é domingo às 12h (199) "
            "e o menor movimento é quinta às 16h (22); quinta é o dia mais "
            "vazio."
        ),
    },
]

COLUNAS_POR_LINHA = 3


def configurar_pagina() -> None:
    st.set_page_config(
        page_title="Dashboard de Gráficos",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",  # a sidebar pode ser recolhida pela seta
    )


def exibir_sidebar() -> None:
    with st.sidebar:
        st.header("👤 Informações do aluno")
        st.markdown(f"**Nome:** {NOME_ALUNO}")
        st.markdown(f"**Nº da chamada:** {NUMERO_CHAMADA}")
        st.markdown(f"**Turma:** {TURMA}")
        st.divider()
        st.caption("Use a seta no topo da barra lateral para recolhê-la.")


def exibir_grafico(item: dict) -> None:
    st.subheader(item["titulo"])
    caminho = PASTA_GRAFICOS / item["arquivo"]
    if caminho.exists():
        st.image(str(caminho))
    else:
        st.error(f"Imagem não encontrada: {caminho.name}")
    st.markdown("**Análise**")
    st.write(item["analise"])


def main() -> None:
    configurar_pagina()
    exibir_sidebar()

    st.title("📊 Dashboard de Visualização de Dados")
    st.write("Gráficos gerados a partir dos arquivos CSV da atividade 06, "
             "com uma breve análise abaixo de cada um.")
    st.divider()

    for inicio in range(0, len(GRAFICOS), COLUNAS_POR_LINHA):
        colunas = st.columns(COLUNAS_POR_LINHA, gap="large")
        for coluna, item in zip(colunas, GRAFICOS[inicio:inicio + COLUNAS_POR_LINHA]):
            with coluna:
                exibir_grafico(item)
        st.divider()


if __name__ == "__main__":
    main()
