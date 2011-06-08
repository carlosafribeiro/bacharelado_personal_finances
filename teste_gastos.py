#coding: utf-8

import unittest
from should_dsl import should
from gasto import Gasto

class TestGastos(unittest.TestCase):

    def teste_registrar_gasto(self):
        gasto1 = Gasto("Bala", "Superfluo", 10, 1.00)
        gasto1.descricao |should| equal_to("Bala")
        gasto1.tipo |should| equal_to("Superfluo")
        gasto1.quantidade |should| equal_to(10)
        gasto1.valor |should| equal_to(1.00)  
        
            
        
if __name__=="__main__":
    unittest.main()
