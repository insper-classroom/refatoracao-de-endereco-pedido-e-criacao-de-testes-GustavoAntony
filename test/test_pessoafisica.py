import pytest
import numpy as np
from classes.Endereco import Endereco
import http.client as httplib
from requests.exceptions import ConnectionError
import requests
import json
from classes.PessoaFisica import PessoaFisica

@pytest.mark.main2
@pytest.mark.teste_pessoa
@pytest.mark.main3
@pytest.mark.teste_com_internet
def test_criacao_pessoa_fisica():
    nome = 'Carlos'
    email = 'tiago@email.com'
    cpf = '524.222.452-6'
    pessoa1 = PessoaFisica(cpf,email,nome)
    assert pessoa1.nome == 'Carlos'

@pytest.mark.main2
@pytest.mark.teste_pessoa
@pytest.mark.teste_com_internet
@pytest.mark.main3
def test_pessoa_adicionar_endereco():
    nome = 'Carlos'
    email = 'tiago@email.com'
    cpf = '524.222.452-6'
    pessoa1 = PessoaFisica(cpf,email,nome)
    end1 = Endereco('08320330', 430)
    pessoa1.adicionar_endereco('casa',end1)
    assert 'Rua Clemente Falcão' == pessoa1.get_endereco('casa')['casa']

@pytest.mark.main2
@pytest.mark.teste_pessoa
@pytest.mark.teste_com_internet
@pytest.mark.main3
def test_pessoa_listar_endereco():
    nome = 'Carlos'
    email = 'tiago@email.com'
    cpf = '524.222.452-6'
    pessoa1 = PessoaFisica(cpf,email,nome)
    end1 = Endereco('08320330', 430)
    pessoa1.adicionar_endereco('casa',end1)
    list = pessoa1.listar_enderecos()
    assert list == {'casa': 'Rua Clemente Falcão'}
    


@pytest.mark.teste_pessoa
@pytest.mark.teste_com_internet
@pytest.mark.main3
def test_pessoa_busca_nome():
    nome = 'Carlos'
    email = 'tiago@email.com'
    cpf = '524.222.452-6'
    pessoa1 = PessoaFisica(cpf,email,nome)
    pessoas = PessoaFisica.busca_nome('Carl')
    if len(pessoas) > 0:
        pessoa = pessoas[0]
    assert pessoa.get_name() == 'Carlos'