import pytest
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json
from classes.Produto import Produto

@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_endereco
def test_criacao_endereco():
    end = Endereco('12232239', 205)
    assert end.rua == 'Rua José Bonifácio de Oliveira'



@pytest.mark.teste_com_internet
@pytest.mark.main3
@pytest.mark.teste_endereco
def test_endereco_consultar_cep():
    cep = 12232239
    rua = Endereco.consultar_cep(cep)['logradouro']
    assert 'Rua José Bonifácio de Oliveira' == rua
