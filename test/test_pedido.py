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

#adicionar um teste master de integração por meio do pedido
@pytest.mark.teste_integracao_pedido
@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_pagamento
def a():
    pass


