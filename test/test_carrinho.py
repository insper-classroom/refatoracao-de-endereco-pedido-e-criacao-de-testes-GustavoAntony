import pytest
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json
from classes.Produto import Produto
from classes.Carrinho import Carrinho

@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_carrinho
def test_criacao_carrinho():
    carrinho = Carrinho()
    assert {} == carrinho.get_itens()


@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_carrinho
def test_carrinho_adicionar_item():
    sabonete = Produto(1,'sabonete')
    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete,4)
    assert {'1': {'sabonete': 4}} == carrinho.get_itens()