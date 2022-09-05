import pytest
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pagamentos import Pagamento
from classes.Pedido import Pedido
import copy

#adicionar um teste master de integração por meio do pedido
@pytest.mark.teste_integracao_pedido
@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_pedido
def test_completo_pedido():
    pessoa1 = PessoaFisica('524.222.452-6', 'tiago@email.com','Carlos')
    endereco = Endereco('08320330', 430)
    item = Produto(21,'banana')
    carrinho = Carrinho()
    carrinho.adicionar_item(item, 5)
    pessoa1.adicionar_endereco('casa', endereco)
    pedido = Pedido(pessoa1,carrinho,endereco)
    pedido.endereco_faturamento = copy.deepcopy(endereco)
    pag = Pagamento(pedido)
    pag.processa_pagamento()
    if pag.pagamento_aprovado():
        pedido.pagamento = 'pago'
    assert "Carlos | Rua Clemente Falcão, número 430 | {'21': {'banana': 5}} | Status: Pedido pago" == pedido.get_pedido()

