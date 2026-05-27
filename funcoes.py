import csv
import re
from datetime import datetime

# classe responsável pelo tratamento do CSV de produtos:
# - trata categorias vazias
# - trata dimensões físicas
# - calcula mediana
# - trata strings 
class TratamentoProdutos:

    # método construtor
    def __init__(self):

        # contador total de linhas processadas
        self.total_linhas = 0

        # contador de categorias corrigidas
        self.categorias_corrigidas = 0

        # contador de dimensões corrigidas
        self.dimensoes_corrigidas = 0

        # dicionário com listas das dimensões
        self.dimensoes = {

            "product_weight_g": [],

            "product_length_cm": [],

            "product_height_cm": [],

            "product_width_cm": []
        }

    
    
    
    # método responsável por calcular mediana
    def calcular_mediana(self, lista):

        # ordena os valores
        lista.sort()

        # tamanho da lista
        tamanho = len(lista)

        # posição do meio
        meio = tamanho // 2

        # verifica se quantidade é ímpar
        if tamanho % 2 != 0:

            # retorna valor central
            return lista[meio]

        # retorna média dos dois valores centrais
        return (lista[meio - 1] + lista[meio]) / 2

   
   
   
   
   
    # método responsável por tratar valores nulos
    def tratar_nulos(self):

        # abre o arquivo CSV
        with open(
            "olist_products_dataset.csv",
            "r",
            encoding="utf-8-sig"
        ) as arquivo:

            # transforma linhas em dicionários
            leitor = csv.DictReader(arquivo)

            # percorre as linhas
            for linha in leitor:

                # limpa chaves do dicionário
                linha = {

                    chave.replace('"', '').strip(): valor

                    for chave, valor in linha.items()
                }

                # percorre dimensões
                for coluna in self.dimensoes:

                    # verifica se valor não está vazio
                    if linha[coluna] != "":

                        # adiciona valor na lista
                        self.dimensoes[coluna].append(
                            float(linha[coluna])
                        )

        # dicionário para armazenar medianas
        medianas = {}

        # calcula mediana de cada dimensão
        for coluna in self.dimensoes:

            medianas[coluna] = (
                self.calcular_mediana(
                    self.dimensoes[coluna]
                )
            )

        # abre novamente o arquivo CSV
        with open(
            "olist_products_dataset.csv",
            "r",
            encoding="utf-8-sig"
        ) as arquivo:

            # transforma linhas em dicionários
            leitor = csv.DictReader(arquivo)

            # percorre todas as linhas
            for linha in leitor:

                # limpa chaves do dicionário
                linha = {

                    chave.replace('"', '').strip(): valor

                    for chave, valor in linha.items()
                }

                # soma +1 para cada linha processada
                self.total_linhas += 1

                # verifica se categoria está vazia
                if linha["product_category_name"] == "":

                    # substitui por Sem Categoria
                    linha["product_category_name"] = (
                        "Sem Categoria"
                    )

                    # soma +1 no contador
                    self.categorias_corrigidas += 1

                # percorre dimensões
                for coluna in self.dimensoes:

                    # verifica se dimensão está vazia
                    if linha[coluna] == "":

                        """
                        Optei por preencher valores
                        nulos utilizando a mediana,
                        pois ela reduz impacto de
                        valores extremos (outliers)
                        e mantém os dados mais
                        próximos da realidade.
                        """

                        # substitui pela mediana
                        linha[coluna] = (
                            medianas[coluna]
                        )

                        # soma +1 no contador
                        self.dimensoes_corrigidas += 1

        # relatório final
        print("\nRELATÓRIO SOBRE PRODUTOS")

        print(
            f"Total de linhas processadas: "
            f"{self.total_linhas}"
        )

        print(
            f"Produtos sem Categoria Corrigidos: "
            f"{self.categorias_corrigidas}"
        )

        print(
            f"Total Dimensões Corrigidas com o Valor da Mediana: "
            f"{self.dimensoes_corrigidas}"
        )

    
    #método responsável por limpar strings
    def limpar_strings(self):

        # contador de strings tratadas
        strings_tratadas = 0


        # abre o CSV
        with open(
            "olist_products_dataset.csv",
            "r",
            encoding="utf-8-sig"
        ) as arquivo:
        
        # transforma linhas em dicionários
            leitor = csv.DictReader(arquivo)
            
            #percorre linhas
            for linha in leitor:

                #pega categoria
                categoria = linha["product_category_name"]

                #verifica se categoria não está vazia
                if categoria != "":

                    #guarda valor original
                    categoria_original = categoria

                    #remove espaços extra
                    categoria = categoria.strip()

                    #transforma em letras minúsculas
                    categoria = categoria.lower()

                    #remove carcteres especiais
                    categoria = re.sub( r"[^a-zA-ZÀ-ÿ\s]",
                        "",
                        categoria
                    )
            


                #verifica se houve alteração
                if categoria != categoria_original:
                   
                    #soma +1 no contador
                    strings_tratadas += 1

                     
                     #atualiza categoria
                linha["product_category_name"] = categoria

                # exibe relatório
            print(
                f"Total de Strings Corrigidas: "
                f"{strings_tratadas}"
                )


        




# classe responsável pelo tratamento do CSV pedidos
class TratamentoPedidos :

    #método construtor
    def __init__(self):

        #contador total de linhas
        self.total_pedidos = 0

        #contador de pedidos cancelados
        self.pedidos_cancelados = 0

        #contador de datas vazias
        self.datas_vazias = 0

    
    
    #método responsável pelas regras de negócio e tratamento de datas

    def tratar_pedidos(self):

        #abre o arquivo CSV
        with open("olist_orders_dataset.csv",
            "r",
            encoding="utf-8-sig") as arquivo:

            #transforma linhas em dicionários
            leitor = csv.DictReader(arquivo)

            #percorre linhas
            for linha in leitor:

                # soma +1 no total
                self.total_pedidos += 1

                #pega status do pedido
                status = linha["order_status"]

                #remove espaços extras
                status = status.strip()

                #transforma em minúsculo
                status = status.lower()
                # remove caracteres especiais
                status = re.sub(r"[^a-zA-Z]", "",status)
            
                # pega data de entrega
                data_entrega = (linha["order_delivered_customer_date"])

                #verifica se data está vazia
                if data_entrega == "":

                    #soma +1 contador
                    self.datas_vazias += 1

                    #verifica se o pedido foi cancelado
                    if status == "canceled":

                        #soma +1 contador
                        self.pedidos_cancelados += 1
                
                #verifica se existe data aprovação
                if linha["order_approved_at"] != "":

                    #converte string para datetime
                    data = datetime.strptime(linha["order_approved_at"], "%Y-%m-%d %H:%M:%S")

                    #converte para formato brasileiro
                    data_brasileira = data.strftime("%d/%m/%Y")

                    #atualiza valor
                    linha["order_approved_at"] = (data_brasileira)
    
        #Relatório Final
        print("\nRELATÓRIO PEDIDOS")
        print(
                f"Total de pedidos processados: "
                f"{self.total_pedidos}"
            )

        print(
                f"Datas de entrega vazias: "
                f"{self.datas_vazias}"
            )

        print(
                f"Pedidos cancelados identificados: "
                f"{self.pedidos_cancelados}"
            )
