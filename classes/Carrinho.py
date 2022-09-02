#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens = {}

    def adicionar_item(self, item:Produto, qtd):
        
        self.id = item.get_id()
        self.quant = qtd
        self.nome = item.get_name()
        self.__itens[f'{self.id}'] = {self.nome:self.quant}
        
        # Implemente a adição do item no dicionário
    def get_itens(self):
        return self.__itens


    def remover_item(self, item:Produto):
        pass
        # Implemente este método
    
    def __str__(self):
        return f'{self.__itens}'
