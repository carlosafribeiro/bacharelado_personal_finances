#coding: utf-8

from datetime import date

class Gasto(object):

    def __init__(self, descricao, tipo, quantidade, valor):
        self.descricao = descricao
        self.tipo = tipo
        self.quantidade = quantidade
        self.valor = valor
        self.data = date.today()

        
   
        
        
        
