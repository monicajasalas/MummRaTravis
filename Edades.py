# -*- coding: utf-8 -*-
class Edades():

	edad = 0

	def obtener_resultado(self):
		return self.edad

	def validar_edad(self, edad):
		try:
			if int(edad) <= 0:
				self.no_existes()
			elif int(edad) >= 1 and int(edad) <=13:
				self.nino()
			elif int(edad)>=14 and int(edad)<=18:
				self.adolesc()
			elif int(edad)>=19 and int(edad)<=65:
				self.adulto()
			elif int(edad)>=66 and int(edad) <=120:
				self.adultomay()
			else:
				self.inmortMR()
		except:
			self.letrasEd()

	def no_existes(self):
		print 'No existes'
		self.edad = 1

	def nino(self):
		print 'Eres niño'
		self.edad = 2

	def adolesc(self):
		print 'Eres adolescente'
		self.edad = 3

	def adulto(self):
		print 'Eres adulto'
		self.edad = 4
	

	def adultomay(self):
		print('Eres adulto mayor')
		self.edad= 5

	def inmortMR(self):
		print'Eres Mumm-Ra'
		self.edad=6

	def letrasEd(self):
		print 'No es una edad'
		self.edad=0