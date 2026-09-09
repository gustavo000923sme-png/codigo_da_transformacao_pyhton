'''
Módulo 12 - Testes automatizados
'''

import unittest


class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        # Executado antes de cada teste
        self.calc = Calculadora()

   
    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_dividir_sucesso(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

   
    def test_divisao_por_zero(self):
       
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
