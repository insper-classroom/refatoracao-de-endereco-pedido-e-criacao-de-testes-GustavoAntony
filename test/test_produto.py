import pytest
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json

from classes.Produto import Produto


@pytest.mark.teste_com_internet
def test_criacao_produto():
    id = 64
    nome = 'banana'
    produto1 = Produto(id,nome)
    assert produto1.get_name() == 'banana'
    
@pytest.mark.teste_com_internet
def test_produto_busca_nome():
    produto2 = Produto(25,'farinha')
    produto_busca = Produto.busca_nome('far')
    assert 'farinha' == produto_busca
