# -*- coding: utf-8 -*-
import kivy
kivy.require('1.7.2')
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Warning(ModalView):
	pass

class Selector(Accordion):
	subtotal = ObjectProperty(None)
	efectivo = ObjectProperty(None)


class Payment(BoxLayout):
	ScreenRoot = None
	Total = 0
	def __init__(self,parent = None,**kwargs):
		super(Payment, self).__init__(**kwargs)
		self.alert = Warning()
		self.ScreenRoot = parent
		print(self.ScreenRoot)
		self.Select = Selector()
		self.add_widget(self.Select)
		self.Select.efectivo.bind(on_text_validate = self.CalcChange)

	def CalcChange(instance,self):
		#print(format_price(int(instance.Total)-int(instance.Select.efectivo.text)))
		print(str(instance.Total).isdigit())
		instance.alert.open()

def format_float(n, decimals=1):#Le da formato a los strings con dinero
    """float -> string"""
    t = {",": ".", ".": ","}
    return "".join(t.get(c, c) for c in format(n, ",.{}f".format(decimals)))

def format_price(p, sym="$", decimals=0):
    """int -> string"""
    if sym == "CL":
        sym = "$"
    return u"{0} {1}".format(sym, format_float(p, decimals=decimals))