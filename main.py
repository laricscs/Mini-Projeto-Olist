from funcoes import (TratamentoProdutos, TratamentoPedidos)


# cria objeto da classe PRODUTOS
produtos = TratamentoProdutos()
# executa método
produtos.tratar_nulos()
produtos.limpar_strings()


# cria objeto da classe PEDIDOS
pedidos = TratamentoPedidos()
pedidos.tratar_pedidos()