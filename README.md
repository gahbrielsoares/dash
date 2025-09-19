# Dashboard E-commerce Estatístico
Este repositório contém um projeto de análise de dados com Python e uma aplicação web interativa usando Dash. O objetivo é permitir que usuários visualizem gráficos e estatísticas de um conjunto de dados de ecommerce sem precisar executar código localmente — basta usar um link.

## 📁 Conteúdo do projeto
- `ecommerce_estatistica.csv` — conjunto de dados contendo informações sobre produtos, avaliações, preços, descontos etc.  
- `estatistica.ipynb` — notebook com análise exploratória, geração de gráficos e visualizações.  
- (Opcional) `estatistica.py` — versão em script Python que gera os gráficos.  
- `requirements.txt` — lista de bibliotecas Python necessárias.  
- `README.md` — este arquivo de descrição do projeto.

## 📊 Funcionalidades
O dashboard permite visualizar:
- Distribuição de preços  
- Relação entre desconto e preço  
- Mapa de calor das correlações entre variáveis numéricas  
- Frequência das marcas mais comuns  
- Distribuição de gênero dos produtos  
- Densidade das notas  
- Regressão entre número de avaliações e nota  

##Como executar localmente
1. Fazer download/clonar este repositório.  
2. Instalar dependências:

   ```bash
   pip install -r requirements.txt

3. Rodar o aplicativo Dash (usando o arquivo principal, por exemplo estatistica.py):
python estatistica.py

4. Abrir o navegador no endereço mostrado no terminal (por padrão http://127.0.0.1:8050/).
