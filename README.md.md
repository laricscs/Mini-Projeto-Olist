# Mini Projeto Avaliativo SCTECH - Olist 

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um pipeline de sanitização de dados utilizando apenas bibliotecas nativas do Python, como `csv`, `re` e `datetime`.

A proposta simula um cenário real da empresa Olist, onde arquivos CSV contendo dados de produtos e pedidos apresentavam inconsistências que comprometiam relatórios automatizados e futuras aplicações de Machine Learning.

Durante o desenvolvimento foram aplicadas técnicas de tratamento de valores nulos, padronização de strings, validação de regras de negócio e formatação de datas, garantindo maior qualidade e confiabilidade dos dados processados.

---

# Funcionalidades Desenvolvidas

## Tratamento de Dados Ausentes

- Preenchimento de categorias vazias com `"Sem Categoria"`
- Tratamento de dimensões físicas nulas utilizando mediana

## Padronização de Strings

- Conversão de textos para letras minúsculas
- Remoção de espaços extras
- Limpeza de caracteres especiais utilizando Regex

## Regras de Negócio

- Identificação de pedidos com data de entrega vazia
- Validação da hipótese de que pedidos sem entrega estavam obrigatoriamente cancelados

## Formatação Temporal

- Conversão de datas do formato original para o padrão brasileiro utilizando `datetime`

## Relatório Final

O sistema exibe:

- Total de linhas processadas
- Quantidade de categorias corrigidas
- Quantidade de dimensões tratadas
- Quantidade de strings padronizadas
- Quantidade de pedidos cancelados identificados

---

# Conclusão da Regra de Negócio

Durante a análise dos pedidos, foi identificado que a hipótese inicial da Olist não era totalmente verdadeira. A empresa acreditava que todas as datas de entrega vazias estavam relacionadas exclusivamente a pedidos cancelados.

Porém, após o processamento dos dados, foram encontrados 2965 pedidos com data de entrega vazia, enquanto apenas 619 possuíam status `"canceled"`.

Isso demonstra que existem outros status de pedidos que também apresentam ausência na data de entrega, indicando possíveis inconsistências operacionais ou fluxos incompletos no processo logístico da plataforma.

---

# Guia de Execução

## 1. Clone o repositório

```bash
git clone https://github.com/laricscs/Mini-Projeto-Olist.git
```

## 2. Acesse a pasta do projeto

```bash
cd Mini-Projeto-Olist
```

## 3. Execute o arquivo principal

```bash
python main.py
```

---

# Estrutura do Projeto

```text
Mini-Projeto-Olist/
│
├── main.py
├── funcoes.py
├── olist_products_dataset.csv
├── olist_orders_dataset.csv
└── README.md
```

---

# Reflexão Teórica sobre Machine Learning

Em projetos de Machine Learning, a qualidade dos dados é um dos fatores mais importantes para garantir modelos confiáveis e eficientes. Existe um conceito muito utilizado na área chamado “Garbage In, Garbage Out” (Lixo Entra, Lixo Sai), que significa que dados incorretos, incompletos ou inconsistentes geram resultados ruins, independentemente da qualidade do algoritmo utilizado.

Por esse motivo, o processo de limpeza e tratamento de dados é essencial antes do treinamento de modelos de Inteligência Artificial. Dados padronizados ajudam a reduzir vieses, inconsistências e problemas como Overfitting, além de melhorar a capacidade do modelo de identificar padrões reais.

Se um modelo de IA for treinado com dados incorretos, categorias inconsistentes ou informações ausentes, ele poderá aprender padrões errados e gerar previsões enviesadas. Isso pode impactar diretamente a tomada de decisão automatizada das empresas.

Neste projeto, técnicas de sanitização como tratamento de valores nulos, limpeza de strings e validação de regras de negócio foram fundamentais para tornar os dados mais confiáveis para futuras análises e aplicações de IA.

---

# Tecnologias Utilizadas

- Python
- CSV
- Regex (`re`)
- Datetime

---

# Autor

Larissa Souza  
Estudante de Engenharia da Computação