#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    lista_pessoas = []
    

    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__enderecos = {}
        self.__showendereco = {}
        PessoaFisica.lista_pessoas.append(self)
        

    
    def __str__(self):
        return f'{self.nome} e {self.__cpf}'
    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[f'{apelido_endereco}'] = end
        self.__showendereco[f'{apelido_endereco}'] = end.rua

        return self.__enderecos

    def remover_endereco(self, apelido_endereco):
        del self.__enderecos[f'{apelido_endereco}']
        del self.__showendereco[f'{apelido_endereco}'] 

    def get_endereco(self, apelido_endereco):
        endereco = self.__enderecos[apelido_endereco]
        rua = self.__showendereco
        return rua

    def listar_enderecos(self):
        return self.__showendereco

    def busca_nome(nome):
        lista = []
        for pessoa in PessoaFisica.lista_pessoas:
            if nome.upper() in pessoa.nome.upper():
                lista.append(pessoa)
        return lista
    