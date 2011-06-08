#coding: utf-8

class Pessoa(object):

    def __init__(self, nome, salario, data_pagamento):
        self.nome = nome
        self.salario = salario
        self.data_pagamento = data_pagamento
        gastos = []
