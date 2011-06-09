#coding: utf-8

from datetime import date

class Pessoa(object):

    def __init__(self, nome, salario, data_pagamento):
        self.nome = nome
        self.salario = salario
        self.data_pagamento = data_pagamento
        self.gastos = []
        
    def registrar_gasto(self, gasto):
        self.gastos.append(gasto)
        
    def mostrar_gastos_do_dia(self):
        total = 0
        gasto_superfluo = 0
        for item in range(len(self.gastos)):
            if self.gastos[item].data == date.today():
                total += self.gastos[item].valor
                if self.gastos[item].tipo == "superfluo":
                    gasto_superfluo += self.gastos[item].valor
        relatorio_dia = {}
        relatorio_dia["Total gasto"] = total
        relatorio_dia["Salario restante"] = self.salario - total
        relatorio_dia["Gasto superfluo"] = gasto_superfluo
        return relatorio_dia
                
        
    def mostrar_gastos_da_semana(self):
        pass
        
    def mostrar_gastos_do_mes(self):
        total = 0
        gasto_superfluo = 0
        for item in range(len(self.gastos)):
            total += self.gastos[item].valor
            if self.gastos[item].tipo == "superfluo":
                gasto_superfluo += self.gastos[item].valor  
        relatorio_mes = {}
        relatorio_mes["Salario"] = self.salario
        relatorio_mes["Gastos fixos"] = total - gasto_superfluo
        relatorio_mes["Gastos superfluos"] = gasto_superfluo
        relatorio_mes["Saldo"] = self.salario - total
        return relatorio_mes 
       
