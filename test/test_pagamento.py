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

@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_pagamento
def test_criacao_pagamento():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(pessoa,carrinho)
    pag = Pagamento(pedido)
    assert pag.get_status() == 'aberto'



@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_pagamento
def test_processa_pagamento():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(pessoa,carrinho)
    pag = Pagamento(pedido)
    pag.processa_pagamento()
    assert pag.get_status() == 'pago'
    


@pytest.mark.teste_com_internet
@pytest.mark.main2
@pytest.mark.main3
@pytest.mark.teste_pagamento
def test_pagamento_aprovado():
    pessoa = PessoaFisica('Carlos', 'tiago@email.com', '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(pessoa,carrinho)
    pag = Pagamento(pedido)
    pag.processa_pagamento()
    bol = pag.pagamento_aprovado()
    assert bol == True

