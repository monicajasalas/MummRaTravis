# -*- coding: utf-8 -*-

import unittest

from Edades import Edades

class TestEdad(unittest.TestCase):

	def setUp(self):
		self.edd = Edades()

	def test_no_existes(self):
		self.edd.validar_edad(-5)
		self.assertEquals(self.edd.obtener_resultado(),1)
	def test_nino_ed(self):
		self.edd.validar_edad(3)
		self.assertEquals(self.edd.obtener_resultado(),2)


	def test_adolesc(self):
		self.edd.validar_edad(15)
		self.assertEquals(self.edd.obtener_resultado(),3)

	def test_adulto(self):
		self.edd.validar_edad(45)
		self.assertEquals(self.edd.obtener_resultado(),4)

	def test_mayor_adulto(self):
		self.edd.validar_edad(95)
		self.assertEquals(self.edd.obtener_resultado(),5)

	def test_imort_vi(self):
		self.edd.validar_edad(244235)
		self.assertEquals(self.edd.obtener_resultado(),6)

	def test_letras_edad(self):
		self.edd.validar_edad('p')
		self.assertEquals(self.edd.obtener_resultado(),0)

if __name__ == '__main__':
	unittest.main()
