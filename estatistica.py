# estatistica.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
from dash import Dash, html, dcc
import base64
import io

# ========== 1. LEITURA DOS DADOS ==========
df = pd.read_csv("ecommerce_estatistica.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# ========== 2. GERAÇÃO DOS GRÁFICOS ==========

# Função auxiliar para converter matplotlib em imagem base64
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return f"data:image/png;base64,{encoded}"

# Gráfico 1: Histograma (Preço)
fig1 = plt.figure(figsize=(8, 6))
sns.histplot(df['preço'], kde=True, bins=30, color='skyblue')
plt.title("Distribuição de Preços")
plt.xlabel("Preço")
plt.ylabel("Frequência")
img1 = fig_to_base64(fig1)

# Gráfico 2: Dispersão (Desconto vs Preço)
fig2 = plt.figure(figsize=(8, 6))
sns.scatterplot(x='desconto', y='preço', data=df)
plt.title("Desconto vs Preço")
plt.xlabel("Desconto (%)")
plt.ylabel("Preço")
img2 = fig_to_base64(fig2)

# Gráfico 3: Mapa de Calor
fig3 = plt.figure(figsize=(10, 8))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Mapa de Calor das Correlações")
img3 = fig_to_base64(fig3)

# Gráfico 4: Barras (Marcas mais frequentes)
fig4 = plt.figure(figsize=(10, 6))
top_marcas = df['marca'].value_counts().head(10)
sns.barplot(x=top_marcas.index, y=top_marcas.values, palette="viridis")
plt.title("Top 10 Marcas Mais Frequentes")
plt.xlabel("Marca")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
img4 = fig_to_base64(fig4)

# Gráfico 5: Pizza (Gênero)
genero_counts = df['gênero'].value_counts()
fig5 = px.pie(names=genero_counts.index, values=genero_counts.values, title='Distribuição de Gênero')

# Gráfico 6: Densidade (Nota)
fig6 = plt.figure(figsize=(8, 6))
sns.kdeplot(df['nota'], shade=True, color='green')
plt.title("Densidade das Notas dos Produtos")
plt.xlabel("Nota")
img6 = fig_to_base64(fig6)

# Gráfico 7: Regressão (Nº Avaliações vs Nota)
fig7 = plt.figure(figsize=(8, 6))
sns.regplot(x='n_avaliações', y='nota', data=df, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Relação entre Nº de Avaliações e Nota")
plt.xlabel("Nº de Avaliações")
plt.ylabel("Nota")
img7 = fig_to_base64(fig7)

# ========== 3. CRIAÇÃO DO APP DASH ==========

app = Dash(__name__)
app.title = "Dashboard E-commerce Estatístico"

app.layout = html.Div([
    html.H1("Dashboard E-commerce", style={"textAlign": "center"}),

    html.H2("1. Distribuição de Preços"),
    html.Img(src=img1, style={"width": "60%"}),

    html.H2("2. Dispersão: Desconto vs Preço"),
    html.Img(src=img2, style={"width": "60%"}),

    html.H2("3. Mapa de Calor das Correlações"),
    html.Img(src=img3, style={"width": "60%"}),

    html.H2("4. Top 10 Marcas"),
    html.Img(src=img4, style={"width": "60%"}),

    html.H2("5. Distribuição de Gênero"),
    dcc.Graph(figure=fig5),

    html.H2("6. Densidade das Notas"),
    html.Img(src=img6, style={"width": "60%"}),

    html.H2("7. Regressão: Nº Avaliações vs Nota"),
    html.Img(src=img7, style={"width": "60%"}),

    html.Hr(),
    html.Footer("Aplicação criada com Dash | Desenvolvido por Você", style={"textAlign": "center", "padding": "20px"})
])

# ========== 4. RODAR SERVIDOR ==========
if __name__ == "__main__":
    app.run(debug=True)

