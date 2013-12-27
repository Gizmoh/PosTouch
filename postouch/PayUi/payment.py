# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Selector(Accordion):
	subtotal = ObjectProperty(None)
	efectivo = ObjectProperty(None)
	efectivo.bind(on_text_validate = CalcChange)


class Payment(BoxLayout):
	ScreenRoot = None
	def __init__(self,parent = None,**kwargs):
		super(Payment, self).__init__(**kwargs)
		self.ScreenRoot = parent
		print(self.ScreenRoot)
		self.Select = Selector()
		self.add_widget(self.Select)
		

def calcChange(instance,self):
	print(int(instance.subtotal.text)-int(instance.efectivo.text))