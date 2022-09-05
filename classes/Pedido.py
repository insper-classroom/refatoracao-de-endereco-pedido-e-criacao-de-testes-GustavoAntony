#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re


class Pedido:
    EM_ABERTO = 1
    PAGO = 2

    def __init__(self, conta_pessoa:PessoaFisica, carrinho:Carrinho, endereco:Endereco):
        self.pessoa = conta_pessoa
        self.carrinho = carrinho
        self.itens = carrinho.get_itens()
        self.endereco_entrega = f'{endereco.rua}, número {endereco.numero}'
        self.endereco_faturamento =''
        self.pagamento = 'em aberto'
        
    def get_pedido(self):
        return f'{self.pessoa.nome} | {self.endereco_entrega} | {self.itens} | Status: Pedido {self.pagamento}'
        
    