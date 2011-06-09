#coding: utf-8

import unittest
from should_dsl import should
from gasto import Gasto
from pessoa import Pessoa

class TestGastos(unittest.TestCase):

    def teste_registrar_gasto(self):
        gasto1 = Gasto("Bala", "Superfluo", 10, 1.00)
        gasto1.descricao |should| equal_to("Bala")
        gasto1.tipo |should| equal_to("Superfluo")
        gasto1.quantidade |should| equal_to(10)
        gasto1.valor |should| equal_to(1.00)
        pessoa = Pessoa("Maria", 1000, 10)
        pessoa.registrar_gasto(gasto1)
        pessoa.gastos |should| have(1).itens
        
    def teste_mostrar_gastos_do_dia(self):
        gasto1 = Gasto("Bala", "superfluo", 10, 1.00)
        gasto1.descricao |should| equal_to("Bala")
        gasto1.tipo |should| equal_to("superfluo")
        gasto1.quantidade |should| equal_to(10)
        gasto1.valor |should| equal_to(1.00)
        pessoa = Pessoa("Maria", 1000, 10)
        pessoa.registrar_gasto(gasto1)
        gasto2 = Gasto("Conta de agua", "Fixo", 1, 100.00)
        pessoa.registrar_gasto(gasto2)
        pessoa.mostrar_gastos_do_dia()["Total gasto"] |should| equal_to(101.00)
        pessoa.mostrar_gastos_do_dia()["Salario restante"] |should| equal_to(899.00)
        pessoa.mostrar_gastos_do_dia()["Gasto superfluo"] |should| equal_to(1.00)
        
    def teste_mostrar_gastos_da_semana(self):
        pessoa = Pessoa("Maria", 1000, 10)
        gasto1 = Gasto("Bala", "superfluo", 10, 1.00)
        pessoa.registrar_gasto(gasto1)
        gasto2 = Gasto("Conta de agua", "Fixo", 1, 100.00)
        pessoa.registrar_gasto(gasto2)
        gasto3 = Gasto("Aluguel", "Fixo", 1, 450.00)
        pessoa.registrar_gasto(gasto3)
        pessoa.mostrar_gastos_da_semana()["Total gasto"] |should| equal_to(551.00)
        pessoa.mostrar_gastos_da_semana()["Gastos fixos"] |should| equal_to(550.00)
        pessoa.mostrar_gastos_da_semana()["Gastos superfluos"] |should| equal_to(1.00)
        pessoa.mostrar_gastos_da_semana()["Saldo"] |should| equal_to(449.00)
        
    def teste_mostrar_gastos_do_mes(self):
        pessoa = Pessoa("Maria", 1000, 10)
        gasto1 = Gasto("Bala", "superfluo", 10, 1.00)
        pessoa.registrar_gasto(gasto1)
        gasto2 = Gasto("Conta de agua", "Fixo", 1, 100.00)
        pessoa.registrar_gasto(gasto2)
        gasto3 = Gasto("Aluguel", "Fixo", 1, 450.00)
        pessoa.registrar_gasto(gasto3)
        pessoa.mostrar_gastos_do_mes()["Salario"] |should| equal_to(1000)
        pessoa.mostrar_gastos_do_mes()["Gastos fixos"] |should| equal_to(550.00)
        pessoa.mostrar_gastos_do_mes()["Gastos superfluos"] |should| equal_to(1.00)
        pessoa.mostrar_gastos_do_mes()["Saldo"] |should| equal_to(449.00)
            
        
if __name__=="__main__":
    unittest.main()
