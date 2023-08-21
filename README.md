# Algoritmo de Previsão de Preço de Ações usando Análise de Dados

## Descrição
Bem-vindo ao repositório do Algoritmo de Previsão de Preço de Ações usando Análise de Dados! Este projeto oferece uma implementação abrangente de um algoritmo de aprendizado de máquina que utiliza técnicas avançadas de análise de dados para prever preços de ações com base em um conjunto diversificado de características.

**Objetivo:**
O principal objetivo deste repositório é fornecer uma solução eficiente para previsão de preços de ações usando técnicas de aprendizado de máquina. O algoritmo foi projetado para lidar com dados históricos de ações e extrair insights significativos das seguintes características:

- Preço de Abertura: O preço de abertura da ação no mercado.
- Volume: A quantidade de ações negociadas durante o período.
- Média Móvel de 5 dias: A média dos preços de fechamento nos últimos 5 dias.
- Média Móvel de 21 dias: A média dos preços de fechamento nos últimos 21 dias.
- Preço Máximo: O preço mais alto atingido durante o período.
- Preço Mínimo: O preço mais baixo atingido durante o período.
- Variação: A diferença entre o preço de fechamento atual e o preço de fechamento anterior.

**Recursos e Destaques:**
- Pré-processamento Avançado: O repositório oferece uma série de etapas de pré-processamento que garantem a qualidade dos dados antes de alimentá-los ao modelo de aprendizado de máquina.
- Modelagem Preditiva: Utiliza algoritmos de regressão para prever preços de ações com base nas características selecionadas.
- Visualização de Resultados: Inclui gráficos interativos que mostram as previsões em comparação com os preços reais, permitindo uma análise visual do desempenho do algoritmo.
- Configuração Flexível: Os parâmetros do algoritmo podem ser ajustados para otimizar o desempenho de acordo com diferentes conjuntos de dados.

**Como Usar:**
1. Clone ou baixe o repositório para sua máquina local.
2. Instale as dependências necessárias listadas no arquivo 'requirements.txt'.
3. Use o Jupyter Notebook fornecido para explorar, pré-processar dados e treinar o modelo.
4. Ajuste os parâmetros do modelo, se necessário, e execute as etapas de treinamento.
5. Avalie o desempenho do modelo usando as métricas fornecidas e visualize as previsões.


Este projeto é uma iniciativa empolgante para explorar e aplicar técnicas de análise de dados e aprendizado de máquina no campo financeiro. A previsão de preços de ações é um desafio complexo e fascinante, e este repositório oferece uma base sólida para iniciar suas próprias investigações nessa área.

## Resultado em gráfico do algoritmo

![image](https://user-images.githubusercontent.com/67965680/211150139-e731103e-66f2-408c-8d9d-7c1f7f2cd927.png)

## Requirements
```
scikit-learn==1.2.0 </br>
yahooquery==2.2.15 </br>
reportlab==3.6.12 </br>
pandas==1.5.2 </br>
numpy==1.24.1 </br>
matplotlib==3.6.2 </br>
tqdm==4.64.1 </br>
```
