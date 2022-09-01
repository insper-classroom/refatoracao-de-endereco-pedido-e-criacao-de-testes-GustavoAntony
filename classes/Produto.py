#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    lista_produtos = []

    def __init__(self, id, nome=''):
        self.__id = id
        self.__nome = nome
        Produto.lista_produtos.append(self)        
    
    def set_id(self, id_now):
        self.__id = id_now
    
    def set_name(self, new_name):
        self.__nome = new_name

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__nome
    
    def __str__(self):
        return f'{self.__id} | {self.__nome}'
    
    def busca_nome(string):
        lista = []
        for produto in Produto.lista_produtos:
            if string.upper() in produto.__nome.upper():
                lista.append(produto)
        return lista
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,new_name):
        if new_name[0] != 'T':
            self.__nome = new_name
    
    @nome.getter
    def nome(self):
        return self.nome